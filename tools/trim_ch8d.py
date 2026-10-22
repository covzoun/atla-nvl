#!/usr/bin/env python3
"""Fourth trim pass for chapters/Chapter_08.md — margin below the 8,500 ceiling.

Same addressing scheme: (index, new_text) into the paragraph grid of the file
as it stands when this script runs. Applied highest index to lowest.
"""
import sys

PATH = "chapters/Chapter_08.md"

E = [
    (35, "Nobody moved for the space of one breath. Then the helmsman leaned on the wheel, the bell began to ring below, and the ship swung its bow toward the black wall and picked up speed. Iroh stood with his hands open at his sides. Jake took one step forward, and then another, until he was standing where Zuko could have reached him without turning his head. He said nothing, and stood there cold from his scalp to his heels, with the blood warm and slow inside his gloves."),
    (40, "The first stones hit the water short of the bow and went up in white columns that stood for a moment, spitting steam, then fell back across the deck as hot rain. Jake felt it sting through his coat and smelled sulfur and scorched brine. The second volley came lower. One boulder passed over the mast so close that the rigging hummed, and another dropped off the port quarter and shoved the ship sideways. Men went to their knees, and someone was shouting a name over and over that Jake could not place."),
    (54, "There was no time to think about what it would cost. Jake caught a double fistful of the tunic at the collar and the shoulder and pulled. The pain that went up his arms was so complete that he made a noise he could not have stopped. His fingers did not hold, then did, then the leather ripped and held again. He hauled backwards on his heels. Kaito's boots dragged on the planks, one foot catching the burning timber and coming free. Ten feet. Fifteen. The warm wet inside his gloves had turned slick."),
    (58, "He turned back. The hose crew had the nozzle up and the pump was hammering, but the stream was thin. It broke on the burning wall in a spatter of white steam and did almost nothing. Behind them the fire spread through a stack of rope and crates, bright and fast. Jake grabbed the slack of the hose behind the nearest man and hauled, taking the weight off his arms, and the pain went through his wrists like wire."),
    (80, "It rose from the broken stern in a thick black column and bent over in the wind and trailed away across the water behind them, so dark he could see it from anywhere."),
    (81, "Below decks the engines labored in an uneven, wheezing cough, and the deck had a slight list that made every step a small correction. The fires aft were out, put out by the crew with the pump and a great many wet blankets, and now the men sat where they had stopped, along the rail and against the hatch coamings, sooty and silent."),
    (92, "\"In what?\" But Iroh knew. Jake watched him know. His eyes went to the davits on the starboard side, and his mouth eased into something that was not a smile. \"I see.\""),
    (98, "Between them the boat dropped from its slings by degrees. Smoke rolled over the rail in a black blanket. Jake coughed and kept feeding the rope through his fists, and when the keel kissed the water he let the line run and found that he could not make his hands open. He had to look at them and tell them to."),
    (100, "It was Iroh. He had come up behind them without a sound, which he could do, large as he was. He did not say anything more. He looked at the stained leather, at Jake's face, at Zuko's back as Zuko swung one leg over the rail, and closed one broad hand around Jake's shoulder and held it there, not hard."),
    (105, "The first stroke put a hot wire through both wrists. The second was worse. By the fifth he had found a rhythm that was not so much strength as refusal, long and level and shallow, using the hinge of his back and keeping his hands as loose on the grips as he could. The linen turned wet under the leather, and he felt it pull free of the cut and stick again with every stroke. He kept rowing."),
    (106, "The smoke ran with them for a while, thick as a wall on either hand. Then it thinned, and the wind turned a little, and the stench of burned iron and boiler tar went pale and drifted away. When it was gone the quiet was enormous. He heard the dip of the oars, the drip of water from the blades, and Zuko breathing behind him, slow and measured through his nose. Somewhere far behind them a ship was still coughing smoke across the sky."),
    (109, "That was nearly all either of them said. Jake did not need more. Zuko's voice came a half-beat before the change of the water, and Jake's body answered it before his mind did, shortening a stroke, leaning on the other oar, easing. He had done this beside Zuko before, in drills and in knots of rope on a hundred nights. Now he did it on the open sea with no hull under them, and it was the one easy thing in a very long day."),
    (113, "The mist came on gradually, then all at once. It crept in from the sea and closed the horizon, and the world shrank to a circle of gray water about the width of a courtyard. Jake rowed through it with his head down. The air had a new smell, faint at first, that he took for the last of the smoke until it thickened into a flat sour sulfur catching at the back of his throat. Beneath it lay something deeper, hot and stony, like a forge with its doors shut."),
    (117, "And on the mountain's shoulder, tier above tier, stood a temple. Its roofs rose in sweeping red-and-gold eaves, each layer narrower than the last, as if a building were trying to climb the sky. Bronze doors glinted at its base. From this far it looked as quiet as a painting."),
    (122, "The shore came up fast. The water went from glass to black stone, a rim of jagged volcanic rock heaped in broken plates. The boat slid in on a long slow swell. Jake shipped the oars, braced his boots, and felt the hull grind onto the rock with a groan that carried a long way over the silent water."),
    (133, "It was an old, familiar weight. The sheath lay flat against his hip, and the grip's linen wrapping lay against the cut in his right palm like a nail. He tightened his fingers on the hilt anyway, and in the dark he counted his heartbeats."),
    (137, "He moved. He crept along the gallery in a crouch, keeping the wall at his shoulder, until the rail fell away from the pillars and gave onto open air. Below him lay a vast chamber, tall as a ship's hold, floored in polished black stone. At the far end loomed a pair of enormous doors, bronze-bound and carved with a flame pattern, taller than any gate in the palace. A knot of men in red-and-gold robes crowded in front of them, their heads shaved and bound in topknots, their hands raised in confusion."),
    (141, "The sages looked at one another. For a long moment nobody moved. Then the boy twisted, and a gust of air burst out of him and shoved Zuko half a pace backward, and the arm around his chest slipped. The boy dropped to the floor and ran, straight at the great bronze doors. A pair of the sages flung themselves at the iron handles. The doors began to swing closed. The boy dove through the narrowing gap, and the doors met behind him with a boom that shook dust from the rafters."),
    (149, "\"It was a noble effort, Prince Zuko,\" Zhao said. It was warm and rich, and pleased. \"But your little smokescreen didn't work.\""),
    (157, "\"You're too late, Zhao!\" Zuko said. His voice was raw, but it did not shake. He lifted his chin and stared up at the commander. \"The Avatar's inside, and the doors are sealed.\""),
    (166, "It started at the seam. A thin line of orange crept down the join between the two great bronze leaves, bright as a wire pulled from a forge, and the light spread along the carved flames until every one of them seemed to burn. The latch of black iron went from dull to red to white, and Jake saw it sag. A low hum rose through the floor into the gallery planks under his knees, and the smell of the temple changed. The sandalwood vanished, and in its place came a clean, scorching smell, the air above a blade on a whetstone."),
    (177, "Then the wave took them, all of them, and flung them backward across the black floor like leaves. A man in red-lacquered armor went past the gallery rail at head height and struck the far wall. He was on his back on the stone, one arm across his face, his cloak smoking."),
    (190, "They ran. The corridors that had been silent half an hour ago were alive with noise: the roar of the mountain, the screech of tearing timber, the crash of falling stone. Walls leaned. Jake ran with his arm clamped against his chest and his boots skidding on the hot flagstones. Zuko ran beside him, keeping pace, one hand always an inch from Jake's sleeve."),
    (199, "Then he hauled the free tail across the steel with both arms from the shoulder. Something in the rope gave with a creak, and the line sighed down along the beam and hung free over the glow. The motion had cost him nothing in the fingers and everything in the palm; the leather went hot, and a wet line ran down inside the right sleeve."),
    (205, "For one long moment the whole world hung underneath them in a bowl of orange light, and the heat on his boots was a living thing. Then the arc brought them over the far lip. He shook his arms apart, the rope unraveled and went back, and they struck the stone on their knees and rolled. Behind them the old floor gave way with a long ripping crack, and the beam sagged and fell in a shower of sparks."),
    (215, "They rowed. Jake did not know how his hands closed on the grips. He knew only that every pull was a long scream with no sound behind it. Zuko worked beside him, teeth bared, shoulders heaving. The heat of the island pressed at their backs like a furnace door, and the sweat on Jake's face turned cold as the first open-water spray came over the bow. The spray on his lips tasted of salt, and under it, ash."),
    (219, "A shape was climbing out of the glow above the island. It was huge and white and shaggy, with a broad flat tail and six legs tucked beneath it, rising on the hot air with a slow, powerful beat. It crossed the red face of the mountain and entered the dark. On its back, for a moment, Jake saw a few small shapes huddled together, tiny against the sky. Then the stars took it."),
    (221, "Zuko did not move. His eyes followed the empty place where the shape had been. His wrists were bare and angry red where the manacles had melted, and he held them loosely in his lap, away from his body. In the glow behind them his face looked very young, and for once entirely unguarded. Jake had seen him furious, and seen him broken. This was something else. Zuko looked like a man who had watched the ground open."),
    (223, "There was no ship. He turned that over once, flatly. The ship was somewhere to the north, trailing smoke for a commander to follow, with Iroh on its deck and a crew who were not going to wake from this. They had one boat, two oars, and a coat each. Behind them a commander who could order fire on a prince was pulling himself up off a floor. Ahead lay a dark sea and a country that had a name for what Zuko was now."),
]


def main():
    text = open(PATH, encoding="utf-8").read()
    paras = text.split("\n\n")
    before = len(text.split())
    for idx, new in sorted(E, key=lambda kv: kv[0], reverse=True):
        if idx >= len(paras):
            print(f"FAIL index {idx} out of range ({len(paras)})")
            return 1
        paras[idx] = new
    out = "\n\n".join(paras)
    open(PATH, "w", encoding="utf-8").write(out)
    after = len(out.split())
    print(f"words {before} -> {after} (delta {after - before})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
