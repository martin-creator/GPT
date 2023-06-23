<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <HelloWorld msg="Medical Drug Assistant" />
    <div v-if="messages.length">
      <div v-for="message in messages" :key="message.id">
        <strong>{{ message.author }}:</strong> {{ message.text }}
      </div>
    </div>

    <form @submit.prevent="sendMessage">
      <input type="text" v-model="newMessage" placeholder="Type your message" />
      <button type="submit">Send</button>
    </form>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'
import HelloWorld from "@/components/HelloWorld.vue";

export default {
  name: "HomeView",
  components: {
    HelloWorld,
  },

  data(){
    return{
      messages: [
        {id: 1, author: "AI", text: "Hello, how can I help you?"},
      ], 
      newMessage: "",
    };
  },

  methods: {
    sendMessage(){
      if(this.newMessage.trim() == ""){
        return;
      }
      this.messages.push({
        id: this.messages.length + 1,
        author: "Human",
        text: this.newMessage.trim(),
      });

      const messageText = this.newMessage.trim();

      axios.get(`http://127.0.0.1:5000/?m=${encodeURI(messageText)}`)
      .then(response => {
        console.log(response);
        const message = {
          id: this.messages.length + 1,
          author: "AI",
          text: response.data.m
        };
        this.messages.push(message);
      })
      .catch(error => {
        console.log(error);
        this.messages.push({
            id: this.messages.length + 1,
            author: "AI",
            text: "Sorry, I don't understand",
        });
      });

      this.newMessage = "";
    },
  },
};
</script>
