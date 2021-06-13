import Link from "next/link";

export default function Navi(props) {
  return (
    <header className="w-full flex justify-between py-5 px-12 bg-custWhite text-custBlue3 sticky top-0 shadow-inner">
      <div className="inline-flex">
        <svg
          stroke="currentColor"
          fill="currentColor"
          stroke-width="0"
          viewBox="0 0 24 24"
          height="2em"
          width="2em"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path d="M19,2.01H6c-1.206,0-3,0.799-3,3v3v6v3v2c0,2.201,1.794,3,3,3h15v-2H6.012C5.55,19.998,5,19.815,5,19.01 c0-0.101,0.009-0.191,0.024-0.273c0.112-0.575,0.583-0.717,0.987-0.727H20c0.018,0,0.031-0.009,0.049-0.01H21v-0.99V15V4.01 C21,2.907,20.103,2.01,19,2.01z M19,16.01H5v-2v-6v-3c0-0.806,0.55-0.988,1-1h7v7l2-1l2,1v-7h2V15V16.01z"></path>
        </svg>
        <h1 className="text-3xl font-medium text-custRed">{props.val.text}</h1>
      </div>
      <div className="inline-flex">
        <NavLinks val={{ link: "/books", text: "Books" }} />
        <NavLinks val={{ link: "/", text: "Records" }} />
        <NavLinks val={{ link: "/checkouts", text: "Checkouts" }} />
      </div>
    </header>
  );

  function NavLinks({ val }) {
    return (
      <Link href={val.link}>
        <a className="hover:text-custRed px-2">{val.text}</a>
      </Link>
    );
  }
}
