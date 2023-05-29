<template>
  <div class="search-bar">
    <div class="text-center">
      <h2>Pretražite po ključnim riječima</h2>
      <form @submit.prevent="onSubmit">
        <input v-model="search" type="search" required :disabled="submitting" />
        <input type="submit" value="Traži" :disabled="submitting" />
      </form>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    searchQuery: {
      type: String,
      default: '',
    },
  },
  data() {
    return {
      search: this.searchQuery || '',
      submitting: false,
    }
  },
  watch: {
    searchQuery() {
      this.search = this.searchQuery
    },
  },
  methods: {
    onSubmit(e) {
      this.submitting = true
      window.location.href = `/search?q=${this.search}`
    },
  },
}
</script>

<style lang="scss" scoped>
.search-bar {
  display: flex;
  justify-content: center;
  padding: 18px 32px;
  border: 4px solid #fff;

  h2,
  form {
    margin: 0;
    display: block;
  }

  h2 {
    font-size: 24px;
    font-weight: 900;
    font-style: italic;
    color: #07f;
  }

  form {
    margin: 10px;

    input {
      border: 1px solid #555058;
      border-radius: 5em;
      background: transparent;
      padding: 0 16px;
      font-size: 13px;
      line-height: 28px;
    }

    input[type='search'] {
      margin-right: -28px;
      width: 220px;
    }

    input[type='submit'] {
      border-color: #07f;
      background: #07f;
      color: #fff;
      text-transform: uppercase;
      font-weight: 900;
      letter-spacing: 0.9px;
    }

    input[disabled],
    input:disabled {
      filter: grayscale(100%);
      cursor: wait;
    }
  }
}
</style>
