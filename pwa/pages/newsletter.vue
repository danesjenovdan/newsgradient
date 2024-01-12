<template>
  <div class="container--fluid flex flex-align--center flex-justify--center flex--column">
    <Header />

    <div class="container--fluid">
      <div v-if="!isMobile" class="flex flex-align--center flex-justify--center">
        <h1>Prijavi se na Newsgradient pregled sedmice!</h1>
      </div>
    </div>

    <Divider v-if="!isMobile" class="w-100" />

    <div class="container my-4">
      <b-row>
        <div class="col-12">
          <div class="newsletter-bar p-lg-5">
            <div v-if="!submitted" class="text-center">
              <h2 v-if="showSubscribe">
                Želiš li uvijek biti u toku s najaktualnijim vijestima iz bosanskohercegovačkih medija, grupisanih prema
                ideološkoj orijentaciji?
              </h2>
              <h2 v-if="!showSubscribe">Uređivanje prijave</h2>
              <p v-if="showSubscribe">
                Prijavi se na Newsgradient newsletter i svake sedmice prati pregled najvažnijih događaja u Bosni i
                Hercegovini. Unesi svoj e-mail kako bi pratio/la kako o tim događajima izvještavaju mediji razvrstani na
                skali lijevo-desno!
              </p>
              <p v-if="!showSubscribe">Prijavljen/a si na newsletter. Ako želiš, možeš se odjaviti ispod.</p>
              <form @submit.prevent="onSubmit">
                <input
                  v-if="showSubscribe"
                  v-model="email"
                  type="email"
                  placeholder="E-mail"
                  required
                  :disabled="submitting"
                />
                <input v-if="showSubscribe" type="submit" value="Prijavi se!" :disabled="submitting" />
                <div v-if="error">Nekaj je šlo narobe, poskusite ponovno :(</div>
              </form>
              <input
                v-if="!showSubscribe"
                type="button"
                value="Odjavi se"
                :disabled="submitting"
                @click="unsubscribe()"
              />
            </div>
            <div v-else class="text-center">
              Hvala na prijavi. Potvrdu registracije poslali smo na Vašu e-mail adresu.
            </div>
          </div>
        </div>
      </b-row>
      <b-row class="justify-content-center">
        <div class="col-8 text-center my-5">
          <h4>
            U nastavku pogledaj kako su četiri najaktuelnija medijska događaja iz protekle sedmice predstavljena u
            Newsgradient pregledu.
          </h4>
        </div>
      </b-row>
      <b-row>
        <div v-for="event in events" :key="event.uri" class="col-lg-6 event-wrapper">
          <div style="background-image: linear-gradient(to right, #0076fe 0%, #e50001 100%); height: 5px"></div>
          <div class="event">
            <a
              :href="`https://newsgradient.org/events/${event.uri}`"
              style="color: #222; font-size: 27px; font-weight: 700; font-style: italic; line-height: 1.2"
              >{{ event.title }}</a
            >
            <div style="margin-bottom: 25px">{{ event.date }}</div>
            <div style="margin: 0 -10px">
              <table style="width: 100%; border: 0; table-layout: fixed">
                <tr>
                  <td style="padding: 0 10px; vertical-align: top">
                    <div style="color: #222; font-size: 18px; font-style: italic; line-height: 1.2; margin-bottom: 15px">
                      Najpopularniji clanak iz lijevo orientisanih medija
                    </div>
                    <newsletter-event-article
                      v-for="article in event.articles_slant_1"
                      :key="article.title"
                      :article="article"
                    />
                  </td>
                  <td style="padding: 0 10px; vertical-align: top">
                    <div style="color: #222; font-size: 18px; font-style: italic; line-height: 1.2; margin-bottom: 15px">
                      Najpopularniji clanak iz desno orientisanih medija
                    </div>
                    <newsletter-event-article
                      v-for="article in event.articles_slant_3"
                      :key="article.title"
                      :article="article"
                    />
                  </td>
                </tr>
              </table>
            </div>
            <hr style="border-color: #222; border-width: 1px 0 0 0; height: 0; width: 100%; margin: 30px 0" />
            <div>
              <a
                :href="`https://newsgradient.org/events/${event.uri}`"
                style="
                  color: #222;
                  font-size: 18px;
                  font-style: italic;
                  line-height: 1.2;
                  text-align: center;
                  margin: 30px 0;
                "
                >Pogledaj kako su mediji izvještavali o događaju.</a
              >
              <table style="width: 100%; border: 0; table-layout: fixed">
                <tr>
                  <td style="padding: 0; vertical-align: bottom">
                    <newsletter-event-media
                      :articles="event.all_articles_slant_1"
                      :media-slant-text="'lijevo orientisani mediji'"
                    />
                    <!-- {% include "newsletter_media.html" with articles=event.all_articles_slant_1 media_slant_text=media_slant_1 %} -->
                  </td>
                  <td style="padding: 0; vertical-align: bottom">
                    <!-- {% include "newsletter_media.html" with articles=event.all_articles_slant_2 media_slant_text=media_slant_2 %} -->
                    <newsletter-event-media
                      :articles="event.all_articles_slant_2"
                      :media-slant-text="'neutralni mediji'"
                    />
                  </td>
                  <td style="padding: 0; vertical-align: bottom">
                    <!-- {% include "newsletter_media.html" with articles=event.all_articles_slant_3 media_slant_text=media_slant_3 %} -->
                    <newsletter-event-media
                      :articles="event.all_articles_slant_3"
                      :media-slant-text="'desno orientisani mediji'"
                    />
                  </td>
                </tr>
              </table>
            </div>
          </div>
        </div>
      </b-row>
    </div>
  </div>
</template>

<script>
import Header from '../components/Header'
import Divider from '../components/Divider'
import { API } from '../api'
import NewsletterEventArticle from '../components/NewsletterEventArticle.vue'
import NewsletterEventMedia from '../components/NewsletterEventMedia.vue'

export default {
  components: {
    Header,
    Divider,
    NewsletterEventArticle,
    NewsletterEventMedia,
  },
  async asyncData({ $axios }) {
    const response = await $axios.get(API.news.newsletter)
    const events = response.data
    return { events }
  },
  data() {
    return {
      email: '',
      submitting: false,
      submitted: false,
      error: false,
      showSubscribe: true,
      subscribedEmail: '',
      subscribedToken: '',
      events: [],
    }
  },
  computed: {
    isMobile() {
      return this.$store.state.sizing.windowWidth <= 768
    },
  },
  mounted() {
    this.subscribedEmail = this.$route.query.email
    this.subscribedToken = this.$route.query.token
    if (this.subscribedEmail && this.subscribedToken) {
      this.isSubscribed()
    }
  },
  methods: {
    onSubmit(e) {
      this.submitting = true

      fetch('https://podpri.lb.djnd.si/api/subscribe/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email: this.email,
          segment_id: 20,
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
    isSubscribed() {
      const endpoint = `https://podpri.lb.djnd.si/api/segments/my?token=${this.subscribedToken}&email=${this.subscribedEmail}&campaign=newsgradient`
      this.submitting = true
      fetch(endpoint)
        .then((response) => {
          return response.json()
        })
        .then((json) => {
          if (json.segments.filter((segment) => segment.id === 20).length > 0) {
            this.showSubscribe = false
          }
          this.submitting = false
        })
        .catch((error) => {
          // eslint-disable-next-line no-console
          console.log(error)
          this.submitting = false
          this.error = true
        })
    },
    unsubscribe() {
      this.submitting = true
      const reqUrl = `https://podpri.lb.djnd.si/api/segments/20/contact/?email=${this.subscribedEmail}&token=${this.subscribedToken}`
      fetch(reqUrl, {
        method: 'DELETE',
      })
        .then((response) => {
          return response.json()
        })
        .then((json) => {
          this.submitting = false
          this.showSubscribe = true
        })
    },
  },
  head: {
    title: 'Newsgradient pregled sedmice',
    meta: [
      {
        hid: 'og:title',
        name: 'og:title',
        content: 'Newsgradient pregled sedmice',
      },
      {
        hid: 'og:description',
        name: 'og:description',
        content:
          'Prijavi se na Newsgradient newsletter i svake sedmice prati pregled najvažnijih događaja u medijima raspoređenim prema ideološkoj orijentaciji.',
      },
      {
        hid: 'twitter:title',
        name: 'twitter:title',
        content: 'Newsgradient pregled sedmice',
      },
      {
        hid: 'twitter:description',
        name: 'twitter:description',
        content:
          'Prijavi se na Newsgradient newsletter i svake sedmice prati pregled najvažnijih događaja u medijima raspoređenim prema ideološkoj orijentaciji.',
      },
      {
        hid: 'description',
        name: 'description',
        content:
          'Prijavi se na Newsgradient newsletter i svake sedmice prati pregled najvažnijih događaja u medijima raspoređenim prema ideološkoj orijentaciji.',
      },
      {
        hid: 'og:image',
        property: 'og:image',
        content: 'https://newsgradient.org/ng-og-prijava.jpg',
      },
      {
        hid: 'twitter:image',
        name: 'twitter:image',
        content: 'https://newsgradient.org/ng-og-prijava.jpg',
      },
    ],
  },
}
</script>

<style lang="scss" scoped>
@import '@/assets/style/variables';

h1 {
  text-align: center;
  font-style: italic;
  margin: 36px 0 25px 0;
  font-weight: 900;
  font-size: 36px;
  color: #3f3942;
  max-width: 60vw;
}

h4 {
  font-style: italic;
  font-weight: 900;
  font-size: 24px;
  color: #3f3942;
}

.event-wrapper {
  margin-bottom: 40px;
}

.event {
  background-color: #fff;
  padding: 25px;
  height: 100%;
}

.newsletter-bar {
  display: flex;
  justify-content: center;
  margin: 24px 0;
  padding: 18px 32px;
  border: 4px solid #fff;
  background-color: #fff;

  h2,
  p,
  form {
    margin: 0;
    display: block;
    margin-bottom: 20px;
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
    margin: 10px;

    input {
      border: 1px solid #555058;
      border-radius: 5em;
      background: transparent;
      padding: 0 16px;
      font-size: 16px;
      line-height: 32px;
    }

    input[type='email'] {
      width: 300px;
      margin-right: -40px;

      @media (max-width: $medium) {
        width: 100%;
        margin-right: 0;
      }
    }

    input[type='submit'] {
      border-color: #07f;
      background: #07f;
      color: #fff;
      text-transform: uppercase;
      font-weight: 900;
      letter-spacing: 0.9px;

      @media (max-width: $medium) {
        margin-top: 10px;
      }
    }

    input[disabled],
    input:disabled {
      filter: grayscale(100%);
      cursor: wait;
    }
  }

  input[type='button'] {
    border: 1px solid #555058;
    border-radius: 5em;
    padding: 0 16px;
    font-size: 13px;
    line-height: 28px;
    border-color: #07f;
    background: #07f;
    color: #fff;
    text-transform: uppercase;
    font-weight: 900;
    letter-spacing: 0.9px;
  }
}
</style>
