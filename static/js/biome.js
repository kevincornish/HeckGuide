            var biomes = ["<img src=\"../static/img/swamplands.png\">", "<img src=\"../static/img/grasslands.png\">", "<img src=\"../static/img/badlands.png\">"];
            var ResGathDate = new Date("Dec 20, 2019 13:00:00 GMT+0100");
            var SwampDate = new Date("Mar 6, 2018 22:00:00 GMT+0100");

            function addZero(i) {
              if (i < 10) {
                i = "0" + i;
              }
              return i;
            }

            Date.prototype.addHours = function (h) {
              this.setHours(this.getHours() + h);
              return this;
            }        
            function biome() {
              var now = new Date().getTime();

              var biometimediff = now - SwampDate;
              var bdays = Math.floor(biometimediff / (1000 * 60 * 60 * 24));
              var bsequence = Math.floor(bdays % 3);
              var bsequencetomorrow = Math.floor((bdays + 1) % 3);
              text = "<p>current biome</p>";
              text += "<div class='biome-pic left'>";
              text += "" + biomes[bsequence] + "";
              text += "</div>";
              text += "<p>next biome</p>";
              text += "<div class='biome-pic right'>";
              text += "" + biomes[bsequencetomorrow] + "";
              text += "</div>";
              document.getElementById("biome").innerHTML = text;
            }
            biome();