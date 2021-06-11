export default function A_book({ values }) {
  return (
    <div>
      <p>{values.title}</p>
      <p>{values.average_rating}</p>
      <button>details</button>
      <br />
    </div>
  );
}
