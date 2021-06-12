import { useRouter } from "next/router";
import api from "../../components/api";

export default function A_book(props) {
  const values = props.data["message"];
  if (!!!values) return <p>Not Found</p>;

  return (
    <div>
      <p>{values.isbn}</p>
      <h2>{values.title}</h2>
      <p>{values.average_rating}</p>
      <button>Issue</button>
      <br />
    </div>
  );
}

export async function getServerSideProps(context) {
  try {
    const { data } = await api.get("/books/" + context.params.isbn);
    return {
      props: { data },
    };
  } catch (e) {
    const data = [];
    return {
      props: { data },
    };
  }
}
