$(function () {
  $.ajax({
    url: 'https://fourtonfish.com/hellosalut/?lang=fr'
  }).done((data) => {
    $('#hello').text(data.hello);
  });
});
