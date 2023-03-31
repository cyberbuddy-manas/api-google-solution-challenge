$(document).ready(function () {
  $("#reqForm").on("submit", function (event) {
    event.preventDefault(); // prevent the default form submit action

    $.ajax({
      type: "POST",
      url: "/predict",
      data: $("#req").val(),
      async: true,
      success: function (data) {
        console.log("Result: " + data);
      },
    });
  });
});
