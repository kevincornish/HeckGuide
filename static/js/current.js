		var quests = ["Resource Gathering","Troop Training","Idol Growth","Monster Slaying","Construction","Troop Training","Dragon Growth","Monster Slaying","Might Growth","Troop Training","Research","Dragon Growth","Monster Slaying","Might Growth"];
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

		function listing() {
			var now = new Date().getTime();
			var questtimediff = now - ResGathDate;
			var hours = Math.floor(questtimediff / (1000 * 60 * 60));
			var sequence = Math.floor(hours % 13);
			
		
			text = "<p>Current Quest:" + quests[sequence] + "</p>";
			document.getElementById("current").innerHTML = text;
		}
		listing();
		setInterval(listing, 1000);