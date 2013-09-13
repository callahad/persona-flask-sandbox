/* 1. JavaScript Library

    <script src="https://login.persona.org/include.js"></script>

*/

/* 2. Login / Logout Buttons */

$('#loginBtn').click( function () { navigator.id.request(); } );
$('#logoutBtn').click( function () { navigator.id.logout(); } );

/* 3. Configure Persona */
// NOTE: loggedInUser changed.

navigator.id.watch({
  loggedInUser: "{{ session.email }}" || null,
  onlogin: function (assertion) {
    // A user wants to log in! Send the assertion to my backend.
    $.post("/login", {"assertion": assertion})
    .done(function () { window.location.reload(); })
    .fail(function () { navigator.id.logout(); });
  },
  onlogout: function () {
    // A user has logged out! Tear down their session.
    $.post("/logout")
    .always(function () { window.location.reload(); });
  }
});
