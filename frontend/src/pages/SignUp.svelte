<!-- svelte-ignore a11y-label-has-associated-control -->
<script>
  import { push } from "svelte-spa-router";
  import swal from "sweetalert";
  let email, password;
  let loading = false;

  async function signIn() {
    try {
      loading = true;
      console.log(email, password);

      const response = await fetch("http://localhost:3001/signup", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ email, password }),
      });
     push("/")
    } catch (err) {
      loading = false;
      swal("Error", err.message, "error");
      console.log(err);
    }
  }
</script>

<div>
  <section class="bg-paper flex flex-col md:flex-row h-screen items-center">
    <div class="bg-blue-600 w-full md:w-1/2 xl:w-1/2 h-screen">
      <img
        src="https://images.unsplash.com/photo-1526666923127-b2970f64b422?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1352&q=80https://images.unsplash.com/photo-1444313431167-e7921088a9d3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1441&q=100"
        alt=""
        class="w-full h-full object-cover"
      />
    </div>

    <div
      class="bg-paper md:max-w-md lg:max-w-full md:mx-auto md:w-1/2 xl:w-1/3 h-screen px-6 lg:px-16 xl:px-12
        flex items-center justify-center"
    >
      <div class="w-full h-100">
        <h1 class="text-xl md:text-4xl font-sans font-bold mt-12">
          Sign in to SYMAIONIC
        </h1>

        <form
          class="mt-6"
          action="#"
          method="POST"
          on:submit|preventDefault={signIn}
        >
          <div>
            <label class="block text-gray-700">Email Address</label>
            <input
              type="email"
              name="User.email_id"
              id="EmailID"
              placeholder="Enter Email Address"
              bind:value={email}
              class="w-full px-4 py-3 rounded-lg bg-gray-200 mt-2 border focus:border-gray-500 focus:bg-white focus:outline-none"
              autoComplete="true"
              required
            />
          </div>

          <div class="mt-4">
            <label class="block text-gray-700">Password</label>
            <input
              type="password"
              name="User.pwd"
              id="PWD"
              placeholder="Enter Password"
              bind:value={password}
              minLength="6"
              class="w-full px-4 py-3 rounded-lg bg-gray-200 mt-2 border focus:border-gray-800
                focus:bg-white focus:outline-none"
              required
            />
          </div>

          <div class="text-right mt-2">
            <a
              href="#/signin"
              class="text-sm font-semibold text-gray-700 hover:text-gray-700 focus:text-gray-700"
            >
              Forgot Password?
            </a>
          </div>

          <button
            type="submit"
            class="w-full block bg-orange-400 hover:bg-orange-400 focus:bg-orange-400 text-white font-medium rounded-lg
              px-4 py-3 mt-6"
          >
            Sign In
          </button>
        </form>

        <hr class="my-6 border-gray-300 w-full" />

        <p class="mt-8">
          Need an account?{" "}

          <a
            href="/signup"
            class="text-blue-500 hover:text-blue-700 font-semibold"
          >
            Sign Up
          </a>
        </p>
      </div>
    </div>
  </section>
</div>
