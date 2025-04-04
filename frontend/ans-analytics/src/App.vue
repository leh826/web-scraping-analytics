<template>
  <div id="app">
    <h1>Dev.Leticia</h1>
    <SearchComponent />
  </div>
</template>

<script>
import SearchComponent from "./components/SearchComponent.vue";

export default {
  components: {
    SearchComponent,
  },
};
</script>

<style>
#app {
  font-family: Arial, sans-serif;
  text-align: center;
  margin-top: 20px;
}
</style>
