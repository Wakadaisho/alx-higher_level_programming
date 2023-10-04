$(document).ready(function () {
  const api = 'https://hellosalut.stefanbohacek.dev/?lang=';
  const getLang = () => {
    const lang = $('INPUT#language_code').val();
    $.getJSON(api + lang, function (data) {
      $('DIV#hello').text(decodeHtml(data.hello));
    });
  };
  $('INPUT#btn_translate').click(function () {
    getLang();
  });
  $('INPUT#language_code').keydown(function (e) {
    e.keyCode === 13 && getLang();
  });
});

function decodeHtml (html) {
  const txt = document.createElement('textarea');
  txt.innerHTML = html;
  return txt.value;
}
