from typing import List
import requests
import random


class AllBookPages:
    per_page = 10
    totalBooks = 4000
    FrappeBase = "https://frappe.io/api/method/frappe-library"

    def __len__(self):
        return int(self.totalBooks / self.per_page)

    def filerUsed(self, temp_books: List[dict]):
        for i in range(len(temp_books)):
            if random.random() < 0.1:
                temp_books[i]["not"] = True
        return temp_books

    def ErrorCheck(self, data):
        val = data.json()
        if data.status_code != 200:
            raise ValueError("Wrong api call - " + str(val["exc"]))
        elif "error" in val:
            raise Exception("Error in params" + str(val["error"]))

    def get_page(self, page: int):
        # check border condition
        itemCount = self.per_page * (page - 1)
        startPage = (itemCount // 20) + 1

        endPage = ((itemCount + self.per_page) // 20) + 1
        books = []

        for i in range(startPage, endPage + 1):
            data = requests.get(self.FrappeBase, params={"page": i})
            self.ErrorCheck(data)
            temp_queue = data.json()["message"]

            # function to filter not availible books here
            availble_books = self.filerUsed(temp_queue)

            books.extend(availble_books)

        lowercut = itemCount - ((startPage - 1) * 20)
        uppercut = lowercut + self.per_page
        return books[lowercut:uppercut]


if __name__ == "__main__":
    vendor = AllBookPages()
    print("got Back", len(vendor.get_page(1)))
