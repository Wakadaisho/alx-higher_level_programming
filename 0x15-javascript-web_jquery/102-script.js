$(document).ready(function () {
  const api = 'https://hellosalut.stefanbohacek.dev/?lang=';
  $('INPUT#btn_translate').click(function () {
    const lang = $('INPUT#language_code').val();
    $.getJSON(api + lang, function (data) {
      $('DIV#hello').text(decodeHtml(data.hello));
    });
  });
});

function decodeHtml (html) {
  const txt = document.createElement('textarea');
  txt.innerHTML = html;
  return txt.value;
}
