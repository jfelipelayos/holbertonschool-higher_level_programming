$(function () {
  $('#btn_translate').click(() => {
    $.ajax({
      url:
        'https://fourtonfish.com/hellosalut/?lang=' + $('#language_code').val()
    }).done((data) => {
      $('#hello').text(data.hello);
    });
  });
});
