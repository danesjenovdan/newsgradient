const apiBase = 'https://newsgradient-api.lb.djnd.si/api/v1';

export async function fetchTopEvents(slant = 2) {
  const res = await fetch(`${apiBase}/news/top-events/?slant=${slant}`);
  return res.json();
}

export async function fetchArticles(eventId) {
  const res = await fetch(`${apiBase}/news/articles/${eventId}/`);
  return res.json();
}
