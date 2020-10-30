importScripts("https://www.gstatic.com/firebasejs/7.16.1/firebase-app.js");
importScripts(
    "https://www.gstatic.com/firebasejs/7.16.1/firebase-messaging.js",
);
// For an optimal experience using Cloud Messaging, also add the Firebase SDK for Analytics.
importScripts(
    "https://www.gstatic.com/firebasejs/7.16.1/firebase-analytics.js",
);

// Initialize the Firebase app in the service worker by passing in the
// messagingSenderId.
firebase.initializeApp({
    apiKey: "AIzaSyDphDMiUUzNRhqwXqtI8-1F6sHJTu0WBmA",
    authDomain: "p7app-df2de.firebaseapp.com",
    databaseURL: "https://p7app-df2de.firebaseio.com",
    projectId: "p7app-df2de",
    storageBucket: "p7app-df2de.appspot.com",
    messagingSenderId: "282452792859",
    appId: "1:282452792859:web:4b685f00218a51d6b7cabe",
    measurementId: "G-TDGSN60RYN"
});

// Retrieve an instance of Firebase Messaging so that it can handle background
// messages.
const messaging = firebase.messaging();

messaging.setBackgroundMessageHandler(function(payload) {
    console.log(
        "[firebase-messaging-sw.js] Received background message ",
        payload,
    );
    // Customize notification here
    const notificationTitle = "Background Message Title";
    const notificationOptions = {
        body: "Background Message body.",
        icon: "/itwonders-web-logo.png",
    };

    return self.registration.showNotification(
        notificationTitle,
        notificationOptions,
    );
});