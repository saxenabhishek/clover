import { createContext, useContext, useState } from "react";
import api from "../api";

export const bookContext = createContext();

export default function useBook() {
  return useContext(bookContext);
}

export function Bookprovider(props) {
  const [tra, setTra] = useState({ title: "", book: null, user: null });
  console.log(useBook);
  function issueBook() {
      console.log(tra)
    if (tra.book === null || tra.user === null) {
      throw "Can't values not set";
    }
    api
      .post("books/issue", {
        isbn: tra.book,
        userId: tra.user,
      })
      .then((res) => {
        console.log(res.status);
      });
  }
  return (
    <bookContext.Provider
      value={{
        tra,
        setTra,
        issueBook,
      }}
    >
      {props.children}
    </bookContext.Provider>
  );
}
