<template>
  <ul class="d-flex justify-content-center">
    <li v-if="page > 1" @click="selectPage(page - 1)">&lt;&lt;</li>
    <li v-if="page > 1" @click="selectPage(1)">1</li>
    <li v-if="page - 1 > 1">...</li>
    <li class="active">{{ page }}</li>
    <li v-if="count - page > 1">...</li>
    <li v-if="count > page" @click="selectPage(count)">{{ count }}</li>
    <li v-if="count > page" @click="selectPage(page + 1)">&gt;&gt;</li>
  </ul>
</template>

<script>
export default {
  name: 'Pagination',
  props: {
    page: {
      type: Number,
      default: 1,
    },
  },
  computed: {
    count() {
      return this.$store.state.blog.pageCount
    },
  },
  methods: {
    selectPage(value) {
      this.$emit('select-page', value)
    },
  },
}
</script>

<style lang="scss" scoped>
ul {
  list-style-type: none;
  padding-left: 0;
}
li {
  cursor: pointer;
  font-size: 1.125rem;
  line-height: 1;
  width: 2.25rem;
  height: 2.25rem;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  &:hover {
    color: #0076fe;
  }
  &.active {
    background-image: linear-gradient(to right, #0076fe 0%, #e50001 100%);
    color: #ededed;
  }
}
</style>
