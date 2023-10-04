$(document).ready(function () {
  $.getJSON({ url: 'https://hellosalut.stefanbohacek.dev/?lang=fr' }, function (data) {
    $('DIV#hello').text(data.hello);
  });
});
