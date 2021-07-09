<template>
  <div class="login-form">
    <form @submit.prevent="loginMethod">
      <input
        type="text"
        name="id"
        class="text-field"
        placeholder="아이디"
        v-model="idValue"
      />
      <input
        type="password"
        name="password"
        class="text-field"
        placeholder="비밀번호"
        v-model="password"
      />
      <input type="submit" value="로그인" class="submit-btn" />
    </form>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "HelloWorld",
  data() {
    return {
      idValue: "",
      password: "",
    };
  },
  methods: {
    loginMethod: async function () {
      try{
        await axios.post("/rest/address/login/", {
          userId: this.idValue,
          password: this.password,
        });
        alert("로그인에 성공하였습니다");
      } catch(e){
        alert("로그인에 실패하였습니다")
      }
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
* {
  box-sizing: border-box;
  font-family: "Noto Sans KR", sans-serif;
  border-radius: 5px;
}
body {
  margin: 0;
  background-color: #1bbc9b;
}
.login-form {
  width: 300px;
  background-color: #eeeff1;
  margin-right: auto;
  margin-left: auto;
  margin-top: 50px;
  padding: 20px;
  text-align: center;
  border: none;
}
.text-field {
  font-size: 14px;
  padding: 10px;
  border: none;
  width: 260px;
  margin-bottom: 10px;
}
.submit-btn {
  font-size: 14px;
  border: none;
  padding: 10px;
  width: 260px;
  background-color: #1bbc9b;
  margin-bottom: 30px;
  color: white;
  cursor: pointer;
}
</style>