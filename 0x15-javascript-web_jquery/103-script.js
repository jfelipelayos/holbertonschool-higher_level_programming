$(function () {
  $(document).on('keypress', (e) => {
    if (e.which === 13 && $('#language_code').is(':focus')) {
      language();
    }
  });
  $('#btn_translate').click(() => {
    language();
  });
});

const language = () => {
  $.ajax({
    url:
      'https://fourtonfish.com/hellosalut/?lang=' + $('#language_code').val()
  }).done((data) => {
    $('#hello').text(data.hello);
  });
};
