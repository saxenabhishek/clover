import { useEffect, useState, useRef } from "react";
import api from "../components/api";
import A_book from "../components/A_book";
import BasicPage from "../components/BasicLayout";

export default function books() {
  let [books, setBooks] = useState([]);
  let [page, setPage] = useState(1);
  let [next, hasnext] = useState(false);
  let [loading, setLoading] = useState(true);
  useEffect(() => {
    setLoading(true);
    api
      .get("/books/", {
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
        <div className="w-1/4 my-4" key={key}>
          <A_book values={b} />
        </div>
      );
    });
  }
  function isPrev() {
    if (page == 1) return true;
    return false;
  }
  function InBetPages() {
    var buttArr = [];
    for (var i = 1; i < 10; i++) {
      buttArr.push(
        <span
          key={i}
          className="rounded-full hover:bg-custRed text-xs p-1 px-2 mx-1 flex items-center justify-center  bg-custBlue3 "
          onClick={(e) => {
            setPage(parseInt(e.target.innerText));
          }}
        >
          {i + page}
        </span>
      );
    }
    return <>{buttArr}</>;
  }
  const butt =
    "bg-custRed mx-2 px-2 bg-custBlue3 bg-custRed shawdow-lg rounded-lg";

  return (
    <BasicPage val={{ text: "All Books" }}>
      <div className="flex flex-col mx-28 m-10 border-4 border-custWhite bg-custBlue2 text-custBlue p-4 px-8 rounded-3xl font-raleway shadow-xl">
        <p className="font-normal text-2xl">Page : {page}</p>
        <div className="flex flex-wrap">
          <BookList />
        </div>
        <div className="mx-auto m-3 px-3 flex items-center text-custWhite">
          <button
            className={butt + " rounded-r-none"}
            disabled={isPrev()}
            onClick={() => {
              hasnext(false);
              setPage(page - 1);
            }}
          >
            Prev
          </button>
          <InBetPages />
          <button
            className={butt + " rounded-l-none"}
            disabled={next}
            onClick={() => {
              setPage(page + 1);
            }}
          >
            Next
          </button>
        </div>
      </div>
    </BasicPage>
  );
}
