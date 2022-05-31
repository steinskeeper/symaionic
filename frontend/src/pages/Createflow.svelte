<script>
  import { push } from "svelte-spa-router";
  import swal from "sweetalert";
  let name, model;

  async function createflow() {
    try {
      console.log(name, model);
      const response = await fetch("http://localhost:3001/createflow", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ name, model }),
      });
      let data = await response.json();
      console.log(data);

      push(`/flow/${data.id}`);
    } catch (err) {
      swal("Error", err.message, "error");
      console.log(err);
    }
  }
</script>

<div class="h-screen flex">
  <!-- Fixed sidebar -->
  <div class="bg-pink-900 w-1/3">
    <!-- Sidebar content -->
    <div class="p-8">
      <h1 class="mt-4 text-white font-bold text-4xl">SYMAIONIC</h1>
    </div>
  </div>
  <!-- Scroll wrapper -->
  <div class="flex-1 flex overflow-hidden">
    <!-- Scrollable container -->
    <div class="flex-1 overflow-y-scroll">
      <nav
        class="bg-white w-full flex relative justify-between items-center px-8 h-20"
      >
        <!-- logo -->
        <div class="inline-flex" />

        <!-- end logo -->

        <!-- search bar -->
        <!-- <div class="hidden sm:block flex-shrink flex-grow-0 justify-start px-2"> -->
        <div class="relative hidden sm:block flex-shrink flex-grow-0">
          <input
            type="text"
            class="bg-purple-white bg-gray-100 rounded-lg border-0 p-3 w-full"
            placeholder="Search somthing..."
            style="min-width:400px;"
          />
          <div class="absolute top-0 right-0 p-4 pr-3 text-purple-lighter">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-5 w-5"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
              />
            </svg>
          </div>
        </div>
        <!-- end search bar -->

        <!-- login -->
        <div class="flex-initial">
          <div class="flex justify-end items-center relative">
            <div class="flex mr-4 items-center">
              <div class="block relative">
                <button
                  type="button"
                  class="inline-block py-2 px-3 hover:bg-gray-200 rounded-full relative "
                >
                  <div class="flex items-center h-5">
                    <div class="_xpkakx">
                      <svg
                        viewBox="0 0 16 16"
                        xmlns="http://www.w3.org/2000/svg"
                        aria-hidden="true"
                        role="presentation"
                        focusable="false"
                        style="display: block; height: 16px; width: 16px; fill: currentcolor;"
                        ><path
                          d="m8.002.25a7.77 7.77 0 0 1 7.748 7.776 7.75 7.75 0 0 1 -7.521 7.72l-.246.004a7.75 7.75 0 0 1 -7.73-7.513l-.003-.245a7.75 7.75 0 0 1 7.752-7.742zm1.949 8.5h-3.903c.155 2.897 1.176 5.343 1.886 5.493l.068.007c.68-.002 1.72-2.365 1.932-5.23zm4.255 0h-2.752c-.091 1.96-.53 3.783-1.188 5.076a6.257 6.257 0 0 0 3.905-4.829zm-9.661 0h-2.75a6.257 6.257 0 0 0 3.934 5.075c-.615-1.208-1.036-2.875-1.162-4.686l-.022-.39zm1.188-6.576-.115.046a6.257 6.257 0 0 0 -3.823 5.03h2.75c.085-1.83.471-3.54 1.059-4.81zm2.262-.424c-.702.002-1.784 2.512-1.947 5.5h3.904c-.156-2.903-1.178-5.343-1.892-5.494l-.065-.007zm2.28.432.023.05c.643 1.288 1.069 3.084 1.157 5.018h2.748a6.275 6.275 0 0 0 -3.929-5.068z"
                        /></svg
                      >
                    </div>
                  </div>
                </button>
              </div>
            </div>

            <div class="block">
              <div class="inline relative">
                <button
                  type="button"
                  class="inline-flex items-center relative px-2 border rounded-full hover:shadow-lg"
                >
                  <div class="pl-1">
                    <svg
                      viewBox="0 0 32 32"
                      xmlns="http://www.w3.org/2000/svg"
                      aria-hidden="true"
                      role="presentation"
                      focusable="false"
                      style="display: block; fill: none; height: 16px; width: 16px; stroke: currentcolor; stroke-width: 3; overflow: visible;"
                    >
                      <g fill="none" fill-rule="nonzero">
                        <path d="m2 16h28" />
                        <path d="m2 24h28" />
                        <path d="m2 8h28" />
                      </g>
                    </svg>
                  </div>

                  <div class="block flex-grow-0 flex-shrink-0 h-10 w-12 pl-5">
                    <svg
                      viewBox="0 0 32 32"
                      xmlns="http://www.w3.org/2000/svg"
                      aria-hidden="true"
                      role="presentation"
                      focusable="false"
                      style="display: block; height: 100%; width: 100%; fill: currentcolor;"
                    >
                      <path
                        d="m16 .7c-8.437 0-15.3 6.863-15.3 15.3s6.863 15.3 15.3 15.3 15.3-6.863 15.3-15.3-6.863-15.3-15.3-15.3zm0 28c-4.021 0-7.605-1.884-9.933-4.81a12.425 12.425 0 0 1 6.451-4.4 6.507 6.507 0 0 1 -3.018-5.49c0-3.584 2.916-6.5 6.5-6.5s6.5 2.916 6.5 6.5a6.513 6.513 0 0 1 -3.019 5.491 12.42 12.42 0 0 1 6.452 4.4c-2.328 2.925-5.912 4.809-9.933 4.809z"
                      />
                    </svg>
                  </div>
                </button>
              </div>
            </div>
          </div>
        </div>
        <!-- end login -->
      </nav>
      <link
        rel="stylesheet"
        href="https://unpkg.com/flowbite@1.4.4/dist/flowbite.min.css"
      />

      <!-- This is an example component -->
      <form class="p-20" on:submit={createflow}>
        <div class="mb-6">
          <label
            for="name"
            class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
            >Flow Name</label
          >
          <input
            type="text"
            id="name"
            bind:value={name}
            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
            placeholder="Enter Flow Name"
            required
          />
        </div>

        <div class="mb-5">
          <svg
            class="w-2 h-2 absolute top-0 right-0 m-4 pointer-events-none"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 412 232"
            ><path
              d="M206 171.144L42.678 7.822c-9.763-9.763-25.592-9.763-35.355 0-9.763 9.764-9.763 25.592 0 35.355l181 181c4.88 4.882 11.279 7.323 17.677 7.323s12.796-2.441 17.678-7.322l181-181c9.763-9.764 9.763-25.592 0-35.355-9.763-9.763-25.592-9.763-35.355 0L206 171.144z"
              fill="#648299"
              fill-rule="nonzero"
            /></svg
          >
          <select
            class="border border-gray-300 rounded-full text-gray-600 h-10 pl-5 pr-10 bg-white hover:border-gray-400 focus:outline-none appearance-none"
            bind:value={model}
          >
            <option>Select a ML Model</option>
            <option>Classifier</option>
            <option>Transformation</option>
            <option>Preditction</option>
            <option>NLP</option>
            <option>Generative</option>
          </select>
        </div>
        <label
          for="password"
          class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
          >Train Your Model</label
        >
        <div class="max-w-2xl mx-auto mb-5">
          <div class="flex items-center justify-center w-full">
            <label
              for="dropzone-file"
              class="flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 dark:hover:bg-bray-800 dark:bg-gray-700 hover:bg-gray-100 dark:border-gray-600 dark:hover:border-gray-500 dark:hover:bg-gray-600"
            >
              <div class="flex flex-col items-center justify-center pt-5 pb-6">
                <svg
                  class="w-10 h-10 mb-3 text-gray-400"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                  xmlns="http://www.w3.org/2000/svg"
                  ><path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"
                  /></svg
                >
                <p class="mb-2 text-sm text-gray-500 dark:text-gray-400">
                  <span class="font-semibold">Click to upload</span> or drag and
                  drop
                </p>
                <p class="text-xs text-gray-500 dark:text-gray-400">
                  SVG, PNG, JPG or GIF (MAX. 800x400px)
                </p>
              </div>
              <input id="dropzone-file" type="file" class="hidden" />
            </label>
          </div>

          <script
            src="https://unpkg.com/flowbite@1.4.0/dist/flowbite.js"></script>
        </div>
        <button
          type="reset"
          class="text-white bg-blue-700 mr-5 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
          >Train and Publish</button
        >
        <button
          type="submit"
          class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
          >Use Pretrained and Publish</button
        >
      </form>
    </div>
  </div>
</div>
