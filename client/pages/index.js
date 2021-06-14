import BasicPage from "../components/BasicLayout";
import Link from "next/link";
export default function Home() {
  return (
    <BasicPage val={{ text: "" }}>
      <main className="flex h-full justify-center items-center">
        <div className="container text-center">
          <h1 className="font-raleway font-bold text-9xl m-10">Clover</h1>
          <p className="font-raleway font-light text-2xl">
            Library management software
          </p>
          <button className="bg-custRed p-2 mx-auto m-12 rounded-md">
            <Link href="/books">Get Started</Link>
          </button>
        </div>
      </main>
    </BasicPage>
  );
}
