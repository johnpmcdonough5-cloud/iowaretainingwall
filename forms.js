/*
 * Sends every form on the site to a GoHighLevel inbound webhook.
 *
 * SETUP: In GHL go to Automation > Create Workflow > add trigger
 * "Inbound Webhook", copy the webhook URL, and paste it below.
 */
var GHL_WEBHOOK_URL = "https://services.leadconnectorhq.com/hooks/Gvvmfiz9m5qveMekUyjZ/webhook-trigger/44b6b600-b07d-4141-8f71-1299f876bb58";

(function () {
  function showMessage(form, text, ok) {
    var msg = form.querySelector(".form-status");
    if (!msg) {
      msg = document.createElement("p");
      msg.className = "form-status";
      msg.setAttribute("role", "status");
      form.appendChild(msg);
    }
    msg.textContent = text;
    msg.style.margin = "0.75rem 0 0";
    msg.style.fontWeight = "600";
    msg.style.color = ok ? "#1a7f37" : "#b42318";
  }

  function handleSubmit(e) {
    e.preventDefault();
    var form = e.target;

    if (GHL_WEBHOOK_URL.indexOf("http") !== 0) {
      showMessage(
        form,
        "Form is not connected yet. Please call us at (319) 320-1833.",
        false
      );
      return;
    }

    var button = form.querySelector('button[type="submit"]');
    var originalLabel = button ? button.textContent : "";
    if (button) {
      button.disabled = true;
      button.textContent = "Sending...";
    }

    var payload = {};
    var data = new FormData(form);
    data.forEach(function (value, key) {
      payload[key] = value;
    });
    payload.page_url = window.location.href;
    payload.page_title = document.title;
    payload.submitted_at = new Date().toISOString();

    fetch(GHL_WEBHOOK_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    })
      .then(function (res) {
        if (!res.ok) throw new Error("Webhook responded " + res.status);
        form.reset();
        showMessage(
          form,
          "Thanks! Your request was sent — we'll be in touch shortly.",
          true
        );
      })
      .catch(function () {
        showMessage(
          form,
          "Something went wrong sending your request. Please call us at (319) 320-1833.",
          false
        );
      })
      .finally(function () {
        if (button) {
          button.disabled = false;
          button.textContent = originalLabel;
        }
      });
  }

  document.addEventListener("DOMContentLoaded", function () {
    var forms = document.querySelectorAll("form");
    for (var i = 0; i < forms.length; i++) {
      forms[i].addEventListener("submit", handleSubmit);
    }
  });
})();
