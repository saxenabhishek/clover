import BasicPage from "../components/BasicLayout";
import useBook, { bookContext } from "../components/context/book";
import { useRouter } from "next/router";
import { useEffect, useState } from "react";
import api from "../components/api";

export default function issue(props) {
  const b = useBook();
  const router = useRouter();
  const [us, setUs] = useState([]);
  useEffect(() => {
    if (b.tra.book === null) {
      router.push("/books");
    }
  }, []);
  useEffect(() => {
    api
      .get("users/get_users")
      .then((res) => {
        setUs(res.data);
      })
      .catch((e) => {
        console.log(e);
      });
  }, []);

  function UserList(props) {
    if (us.length === 0) {
      return <p className="mx-auto text-xl font-light">No matching users</p>;
    }
    if (typeof us.map !== "function") {
      return <p>Returning book</p>;
    }
    return us.map((i, k) => {
      function handelClick(e) {
        var T = b.tra;
        T.user = i._id;
        setUs(T);
        b.issueBook();
        router.push("/checkouts");
      }
      return (
        <div key={k} className="flex justify-between">
          <div className="flex justify-between relative  w-1/3">
            <p className="text-lg font-bold mx-5">{i.name}</p>
            <p className="">{"LibID." + i._id}</p>
          </div>
          <button
            onClick={handelClick}
            className="rounded-md px-10 py-2 m-2 bg-custBlue2 hover:bg-custRed text-custWhite shadow-md"
          >
            Select
          </button>
        </div>
      );
    });
  }

  function Changing(e) {
    api
      .get("users/get_users", {
        params: {
          name: e.target.value,
        },
      })
      .then((res) => {
        setUs(res.data);
      })
      .catch((e) => {
        console.log(e);
      });
  }
  return (
    <BasicPage val={{ text: "Issuing " + b.tra.title }}>
      <div className="Container bg-custWhite mx-auto w-3/4 p-5 text-custBlue3 flex flex-col rounded-lg shadow-xl border-4 border-custBlue2">
        <div className="m-3">
          <label className="text-lg ">Search </label>
          <input onChange={Changing} className="bg-custBlue rounded-md"></input>
        </div>
        <UserList />
      </div>
    </BasicPage>
  );
}
