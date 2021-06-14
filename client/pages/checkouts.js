import { useEffect, useState } from "react";
import api from "../components/api";
import BasicPage from "../components/BasicLayout";

export default function Checkout(prop) {
  const [us, setUs] = useState([]);
  const [refbu, setRefbu] = useState(false);
  const [topay, setTopay] = useState("Checkouts");
  useEffect(() => {
    api
      .get("/recs", {
        params: {
          completed: false,
        },
      })
      .then((res) => {
        setUs(res.data);
      })
      .catch((e) => {
        console.log(e);
        setTopay("No more checkouts");
      });
  }, [refbu]);
  function TraList(props) {
    if (us.length === 0) {
      return <p className="mx-auto">Looking now...</p>;
    }
    return (
      <table className="table-auto">
        <thead>
          <tr>
            <th>Name</th>
            <th>Book</th>
            <th>When</th>
            <th>Approximate Cost</th>
            <th>Tranaction ID</th>
          </tr>
        </thead>
        <tbody>
          {us.map((i, k) => {
            function handelClick() {
              api
                .put("books/return", {
                  traId: i._id,
                })
                .then((res) => {
                  const c = res.data["message"]["cost"];
                  setTopay("Have to collect ₹" + c + "");
                  setRefbu(!refbu);
                });
            }
            const time = new Date(i.when);
            const now = new Date();
            var x = now - time;
            console.log(x);
            x = ((x / 1000) * 0.002).toFixed(2);
            console.log(x);
            return (
              <tr key={k} className="">
                <td className="p-2">{i.name}</td>
                <td className="p-2">{i.bookTitle}</td>
                <td className="p-2">{time.toLocaleDateString()}</td>
                <td className="p-2">{"₹" + x}</td>
                <td className="p-2">{i._id}</td>
                <button
                  onClick={handelClick}
                  className="bg-custRed p-2 rounded-md m-2 text-custWhite"
                >
                  Return
                </button>
              </tr>
            );
          })}
        </tbody>
      </table>
    );
  }
  return (
    <BasicPage val={{ text: topay }}>
      <div className="Container bg-custWhite mx-auto w-3/4 p-5 text-custBlue3 flex flex-col rounded-lg shadow-xl border-8 border-custBlue2">
        <TraList />
        <button
          className="bg-custBlue2 mx-auto p-3 rounded-md text-white"
          onClick={() => {
            setRefbu(!refbu);
            setUs([]);
          }}
        >
          Refresh
        </button>
      </div>
    </BasicPage>
  );
}
