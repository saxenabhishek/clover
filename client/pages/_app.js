import "../styles/globals.css";
import { Bookprovider } from "../components/context/book";
function MyApp({ Component, pageProps }) {
  return (
    <Bookprovider>
      <Component {...pageProps} />
    </Bookprovider>
  );
}

export default MyApp;
