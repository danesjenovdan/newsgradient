<template>
  <div class="newsletter-bar">
    <div v-if="!submitted" class="text-center">
      <h2><a href="https://newsgradient.org/newsletter">Želiš li uvijek biti u toku sa pregledom objava?</a></h2>
      <p>Prijavi se na newsletter tako što ćeš unijeti svoj email!</p>
      <form @submit.prevent="onSubmit">
        <input v-model="email" type="email" placeholder="email" required :disabled="submitting" />
        <input type="submit" value="Prijavi se" :disabled="submitting" />
        <div v-if="error">Nekaj je šlo narobe, poskusite ponovno :(</div>
      </form>
    </div>
    <div v-else class="text-center">Hvala na prijavi. Za potvrdu registracije provjerite Vaš e-mail.</div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      email: '',
      submitting: false,
      submitted: false,
      error: false,
    }
  },
  methods: {
    onSubmit(e) {
      this.submitting = true

      fetch('https://podpri.djnd.si/api/subscribe/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email: this.email,
          segment: 19,
        }),
      })
        .then((res) => {
          if (res.ok) {
            return res.text()
          }
          throw new Error('Response not ok')
        })
        .then((res) => {
          this.submitted = true
          this.submitting = false
          this.error = false
        })
        .catch((error) => {
          // eslint-disable-next-line no-console
          console.log(error)
          this.submitting = false
          this.error = true
        })
    },
  },
}
</script>

<style lang="scss" scoped>
.newsletter-bar {
  display: flex;
  justify-content: center;
  padding: 18px 32px;
  border: 4px solid #fff;

  h2,
  p,
  form {
    margin: 0;
    display: inline-block;
  }

  h2 {
    font-size: 24px;
    font-weight: 900;
    font-style: italic;
    color: #07f;
  }

  p {
    font-size: 18px;
  }

  form {
    display: flex;
    justify-content: center;
    margin: 10px;

    input {
      border: 1px solid #555058;
      border-radius: 5em;
      background: transparent;
      padding: 0 16px;
      font-size: 13px;
      line-height: 28px;
    }

    input[type='email'] {
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
