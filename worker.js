// Worker перед статикой:
//  - www → основной домен (301);
//  - адрес страницы без слэша на конце → со слэшем (301, а не 307 по умолчанию);
//  - всё остальное — файлы из public/.
export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.hostname === "www.parimatch-betting-india.com") {
      url.hostname = "parimatch-betting-india.com";
      return Response.redirect(url.toString(), 301);
    }
    const last = url.pathname.split("/").pop();
    if (last && !last.includes(".")) {
      url.pathname += "/";
      return Response.redirect(url.toString(), 301);
    }
    return env.ASSETS.fetch(request);
  },
};
