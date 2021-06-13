import Link from "next/link";
import router from "next/router";
import { useEffect } from "react";
import useBook from "./context/book";

export default function A_book({ values }) {
  const b = useBook();

  function titleHelper(val) {
    return val.length > 50 ? val.substring(0, 50) : val;
  }
  useEffect(() => {
    if (typeof values.authors.split === "function") {
      values.authors = values.authors.split("/");
      if (values.authors.length > 50) {
        values.authors = values.authors.substring(0, 50);
      }
    }
  }, []);
  function handelClick() {
    console.log(b);
    let t = b.tra;
    t.book = values.isbn;
    t.title = values.title;
    b.setTra(t);
    router.push("/issue");
  }
  return (
    <div className="bg-custBlue3 mx-5 text-custWhite my-1 py-5 px-3 rounded-md">
      <div className={"p-2 h-36 rounded-md rounded-r-xl "}>
        <p className="text-xl font-semibold">{titleHelper(values.title)}</p>
        <p className="text-lg font-light">{values.authors}</p>
      </div>
      <p>Rating : {values.average_rating}</p>
      <NavBut vals={{ link: "/book/" + values.isbn, title: "Details" }} />
      <NavButIss
        vals={{ link: "/issue", title: "Issue", click: handelClick }}
      />
      <br />
    </div>
  );

  function NavBut({ vals }) {
    return (
      <Link href={vals.link}>
        <button className="bg-custRed rounded-lg mx-1 p-1 text-custWhite w-15">
          {vals.title}
        </button>
      </Link>
    );
  }
  function NavButIss({ vals }) {
    return (
      <Link href={vals.link}>
        <button
          onClick={vals.click}
          className="bg-custRed rounded-lg mx-1 p-1 text-custWhite w-15"
        >
          {vals.title}
        </button>
      </Link>
    );
  }
}
