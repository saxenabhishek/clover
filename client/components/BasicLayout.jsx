import Navi from "./navi";
import Footer from "./footer";
import Head from "next/head";

export default function BasicPage(props) {
  return (
    <div className="flex flex-col h-screen justify-between">
      <Head>
        <title>Clover</title>
        <meta name="description" content="Generated by create next app" />
        <link rel="icon" href="/fav.svg" />
      </Head>
      <Navi val={{ text: props.val.text }} />
      {props.children}
      <Footer />
    </div>
  );
}
