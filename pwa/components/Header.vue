<template>
  <div class="ng-header container--fluid">
    <div class="flex flex-justify--space-between flex-wrap flex-lg-nowrap w-90 mx-auto px-3">
      <div class="flex header-container">
        <nuxt-link to="/" class="flex">
          <h1 hidden>NEWSGRADIENT</h1>
          <img src="@/assets/svg/logo-text.svg" class="logo-image" />
        </nuxt-link>
        <!-- <h2 class="ng-header__text">
          Najaktuelnije vijesti u izvještajima bosanskohercegovačkih <br />
          medija grupisane po ideološkoj orijentaciji.
        </h2> -->
      </div>
      <div class="links-container">
        <!-- <nuxt-link :class="['link', { 'link--active': '/' === $route.path }]" to="/" class="link events-link">
          Vijesti
        </nuxt-link> -->
        <nuxt-link :class="['link', { 'link--active': '/blog' === $route.path }]" to="/blog" class="link">
          Blog
        </nuxt-link>
        <nuxt-link :class="['link', { 'link--active': '/about' === $route.path }]" to="/about" class="link">
          Više o
        </nuxt-link>
        <!-- <a href="https://play.google.com/store/apps/details?id=org.newsgradient.app" class="link events-link">
          Android aplikacija
        </a> -->
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'Header',
  data() {
    return {
      links: [
        { to: '/', title: 'Vijesti' },
        { to: '/about', title: 'Više o' },
      ],
    }
  },
  methods: {
    timerangeChanged(value) {
      this.$store.dispatch('events/setTimerange', value)
    },
  },
}
</script>

<style lang="scss" scoped>
@import '@/assets/style/variables';

.ng-header {
  background-color: #fff;
  top: 0;
  left: 0;
  width: 100%;
  box-shadow: 0px -10px 20px 10px rgba(0, 0, 0, 0.25);
  padding: 10px 0;

  @media (min-width: $small) {
    padding: 32px 0;
  }

  &__text {
    @media (max-width: $medium) {
      display: none;
    }
  }
}

.logo-link {
  text-decoration: none;
  display: block;
}

.logo-image {
  width: 150px;

  @media (min-width: $small) and (max-width: $xlarge) {
    width: 300px;
  }

  @media (min-width: $xlarge) {
    width: 408px;
  }
}

h2 {
  font-size: 18px;
  font-weight: 300;
  font-style: italic;
  line-height: 1.2;
  margin: 0 0 0 0.5rem;
}

.header-container {
  @media (max-width: $small) {
    width: 100%;
    justify-content: center;
  }
}

.links-container {
  display: flex;
  gap: 2rem;
  justify-content: flex-end;
  align-items: center;
  max-width: 450px;
  min-width: 350px;

  @media (max-width: $small) {
    justify-content: center;
  }

  @media (max-width: $large) {
    max-width: 100%;
    width: 100%;
    min-width: 0;
    margin-top: 1em;
  }
}

.link {
  color: #3f3942;
  font-size: 19px;
  font-weight: 900;
  border-bottom: 4px solid white;

  @media (max-width: $small) {
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
    font-size: 10px;
    background-color: #ea4243;
    color: white;
    // width: 20%;
    // flex-grow: 0;
    // flex-shrink: 0;
    // flex-basis: 0%;
    border-radius: 12px;
    border: none;
    font-weight: 400;
    padding: 5px 10px;
  }

  &:hover {
    color: #ea4243;
    border-bottom: 4px solid #ea4243;

    @media (max-width: $small) {
      color: white;
      text-decoration: none;
      border: none;
    }
  }

  &--active {
    color: #ea4243;
    border-bottom: 4px solid #ea4243;

    @media (max-width: $small) {
      color: white;
      text-decoration: none;
      border: none;
    }
  }
}

// .events-link {
//   display: none;

//   @media (min-width: $large) {
//     display: block;
//   }
// }

// .timing-container {
//   display: block;

//   @media (min-width: $large) {
//     display: none;
//   }
// }

a {
  text-decoration: none;
}
</style>
