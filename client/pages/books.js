import { useEffect, useState } from "react";
import api from "../components/api";
import A_book from "../components/A_book";

export default function books() {
  let [books, setBooks] = useState([]);
  let [page, setPage] = useState(1);
  useEffect(() => {
    api
      .get("/books", {
        params: {
          page: page,
        },
      })
      .then((data) => setBooks(data.data["message"]));
  }, [page]);

  function BookList(params) {
    if (books.length === 0) {
      return <p>Loading...</p>;
    }
    return books.map((b, key) => {
      return (
        <div key={key}>
          <A_book values={b} />
        </div>
      );
    });
  }
  return (
    <div>
      <BookList />
      <button disabled={() => !!page} onClick={() => setPage(page - 1)}>
        Prev
      </button>
      <button onClick={() => setPage(page + 1)}>Next</button>
    </div>
  );
}
