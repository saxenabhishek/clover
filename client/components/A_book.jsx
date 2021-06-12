import Link from "next/link";

export default function A_book({ values }) {
  return (
    <div>
      <p>{values.title}</p>
      <p>{values.average_rating}</p>
      <Link href={"book/" + values.isbn}>
        <button>details</button>
      </Link>
      <button>issue</button>
      <br />
    </div>
  );
}
