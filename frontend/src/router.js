import Home from "./pages/Home.svelte";
import NotFound from "./pages/NotFound.svelte";
import SignIn from "./pages/SignIn.svelte";
import SignUp from "./pages/SignUp.svelte";
import Aistore from "./pages/Aistore.svelte";
import Createflow from "./pages/Createflow.svelte";
import Flow from "./pages/Flow.svelte";
const routes = {
  // Exact path
  "/": Home,
  "/signin": SignIn,
  "/signup": SignUp,
  "/aistore": Aistore,
  "/createflow": Createflow,
  "/flow/:id": Flow,

  //   // Using named parameters, with last being optional
  //   "/author/:first/:last?": Author,

  //   // Wildcard parameter
  //   "/book/*": Book,

  // navigate progammatically
  //     import {push, pop, replace} from 'svelte-spa-router'

  // // The push(url) method navigates to another page, just like clicking on a link
  // push('/book/42')

  // // The pop() method is equivalent to hitting the back button in the browser
  // pop()

  // // The replace(url) method navigates to a new page, but without adding a new entry in the browser's history stack
  // // So, clicking on the back button in the browser would not lead to the page users were visiting before the call to replace()
  // replace('/book/3')

  // Get params from url
  //     <p>Your name is: <b>{params.first}</b> <b>{#if params.last}{params.last}{/if}</b></p>
  // <script>
  // //You need to define the component prop "params"
  // export let params = {}
  // </script>

  // Catch-all
  // This is optional, but if present it must be the last
  "*": NotFound,
};

export default routes;
