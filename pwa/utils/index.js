export function baseUrl(url) {
  if (url) {
    const sliceEnd = url.indexOf('/', url.indexOf('://') + 3)
    return url.substring(0, sliceEnd)
  }
  return url
}

export function faviconIcon(url) {
  if (url) {
    return `https://www.google.com/s2/favicons?sz=32&domain_url=${baseUrl(url)}`
  }
  return 'https://www.google.com/s2/favicons?sz=32&domain_url=https://does.not.exist.newsgradient-pwa.lb.djnd.si'
}
