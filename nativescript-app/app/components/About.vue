<template>
  <Page>
    <ActionBar flat="true" class="action-bar">
      <Label text="About Newsgradient" textWrap="true" class="title" />
    </ActionBar>
    <ScrollView>
      <StackLayout class="main-view">
        <GridLayout rows="auto, auto" class="title-container">
          <Label row="0" text="Karta medija" textWrap="true" class="title" />
          <StackLayout row="1" class="gradient-line" />
        </GridLayout>
        <StackLayout class="content-container">
          <NSImg
            src="https://newsgradient.org/Media-Bias-Chart-Bosnia-2.jpg"
            stretch="aspectFit"
            class="karta-medija"
          />
        </StackLayout>
        <GridLayout rows="auto, auto" class="title-container">
          <Label
            row="0"
            text="Šta je Newsgradient?"
            textWrap="true"
            class="title"
          />
          <StackLayout row="1" class="gradient-line" />
        </GridLayout>
        <StackLayout class="content-container">
          <HtmlView :html="staJeHtml" />
        </StackLayout>
        <GridLayout rows="auto, auto" class="title-container">
          <Label
            row="0"
            text="Kako je određena ideološka orijentacija medija?"
            textWrap="true"
            class="title"
          />
          <StackLayout row="1" class="gradient-line" />
        </GridLayout>
        <StackLayout class="content-container">
          <HtmlView :html="ideoloskaOrijentacijaHtml" />
        </StackLayout>
        <GridLayout rows="auto, auto" class="title-container">
          <Label
            row="0"
            text="Kako radi Newsgradient?"
            textWrap="true"
            class="title"
          />
          <StackLayout row="1" class="gradient-line" />
        </GridLayout>
        <StackLayout class="content-container">
          <HtmlView :html="kakoRadiHtml" />
        </StackLayout>
        <GridLayout rows="auto, auto" class="title-container">
          <Label row="0" text="Razvili" textWrap="true" class="title" />
          <StackLayout row="1" class="gradient-line" />
        </GridLayout>
        <StackLayout class="content-container">
          <HtmlView :html="razviliHtml" />
        </StackLayout>
      </StackLayout>
    </ScrollView>
  </Page>
</template>

<script>
export default {
  data() {
    return {
      staJeHtml: `
        Newsgradient je online platforma koja nam omogućava da vidimo kako su mediji iz BiH, grupisani prema svojoj
        ideološkoj orijentaciji, izvještavali o pojedinim događajima i temama.
      `,
      ideoloskaOrijentacijaHtml: `
        Koristeći jedinstvenu metodologiju koju je razvila Vanessa Otero, osnivačica
        <a href="https://www.adfontesmedia.com/" target="_blank">Ad Fontes Media</a>, ocijenili smo pouzdanost i
        ideološku orijentaciju medija u BiH. Tim analitičara/ki je u periodu od dva mjeseca pratio i ocjenjivao uzorak
        medijskih izvještaja odabranih medija prema spomenutoj metodologiji. Na ovaj način su dobijeni ukupni rezultati
        i izračunate ocjene 1) pouzdanosti 2) ideološke orijentacije svakog medija iz uzorka.
        <br><br>
        Više o metodologiji ocjenjivanja medija možete saznati
        <a href="https://www.adfontesmedia.com/how-ad-fontes-ranks-news-sources/" target="_blank">ovdje</a>.
      `,
      kakoRadiHtml: `
        Prikupljamo članke iz odabranih bosanskohercegovačih medija uz pomoć naših saradnika i prijatelja iz
        <a href="https://eventregistry.org/" target="_blank">Event Registry</a>. Novinski članci o istoj temi ili
        događaju se grupiraju. Teme ili događaji o kojima se najviše izvještavalo u proteklom danu su prikazani na
        početnoj stranici. Mediji su, prema ideološkoj orijentaciji, grupisani u tri grupe: lijevo orijentisani mediji,
        neutralni/uravnoteženi mediji i desno orijentisani mediji. Granica koja dijeli ove tri kategorije je
        postavljena prema smjernicama postavljenim od strane autorke metodologije, uvažavajući lokalni kontekst i
        realnost medijske scene u BiH.
      `,
      razviliHtml: `
        <div style="text-align: center;">
          <a href="https://danesjenovdan.si/" target="_blank">Danes je nov dan</a>
        </div>
        <div style="text-align: center;">
          <a href="https://zastone.ba/" target="_blank">ZaštoNe?</a>
        </div>
        <div style="text-align: center;">
          <a href="https://www.adfontesmedia.com/" target="_blank">ad fontes media</a>
        </div>
        <div style="text-transform: uppercase; font-weight: 700; text-align: center;">Uz pomoć</div>
        <div style="text-align: center;">
          <a href="https://www.ned.org/" target="_blank">NED</a>
        </div>
      `,
    };
  },
};
</script>

<style lang="scss" scoped>
@import '@nativescript/theme/scss/variables';

.action-bar {
  @include colorize($background-color: 'background');

  .title {
    margin: 8 40 0 40;
    padding: 0;
    font-style: italic;
    text-align: center;
  }
}

.main-view {
  @include colorize($background-color: 'background-alt-5');

  .title-container {
    margin: 12 40 0 40;

    .title {
      font-size: 14;
      font-weight: 700;
      text-align: center;
      text-transform: uppercase;
    }

    .gradient-line {
      height: 2;
      background-image: linear-gradient(to right, #0076fe 0%, #e50001 100%);
    }
  }

  .content-container {
    @include colorize($background-color: 'background');

    padding: 12;
    font-size: 16;
  }
}
</style>
