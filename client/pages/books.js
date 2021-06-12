import { useEffect, useState, useRef } from "react";
import api from "../components/api";
import A_book from "../components/A_book";

export default function books() {
  let [books, setBooks] = useState([]);
  let [page, setPage] = useState(1);
  let [next, hasnext] = useState(false);
  let [loading, setLoading] = useState(true);
  useEffect(() => {
    setLoading(true);
    api
      .get("/books", {
        params: {
          page: page,
        },
      })
      .then((data) => {
        setLoading(false);
        setBooks(data.data["message"]);
      })
      .catch((err) => {
        console.log(err);
        setLoading(false);
        hasnext(true);
        setPage(page - 1);
      });
  }, [page]);

  function BookList(params) {
    if (loading) {
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
  function isPrev() {
    if (page == 1) return true;
    return false;
  }

  return (
    <div>
      <h1>All Books</h1>
      <p>Page : {page}</p>
      <BookList />
      <button
        disabled={isPrev()}
        onClick={() => {
          hasnext(false);
          setPage(page - 1);
        }}
      >
        Prev
      </button>
      <button
        disabled={next}
        onClick={() => {
          setPage(page + 1);
        }}
      >
        Next
      </button>
    </div>
  );
}
