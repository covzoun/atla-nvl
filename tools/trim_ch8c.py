#!/usr/bin/env python3
"""Third trim pass for chapters/Chapter_08.md.

Same addressing scheme as trim_ch8b.py: (index, new_text) into the paragraph
grid of the file as it stands when this script runs. None deletes a paragraph.
Applied from the highest index to the lowest so no earlier index can shift.
"""
import sys

PATH = "chapters/Chapter_08.md"

E = [
    (2, "It was not the sharp wet cold of the open sea. This was a flat, heavy chill with a haze in it, the sky and the water the same dull colour, and in the air a faint bitterness he knew before he could name it. Smoke from somewhere far off, thinned by distance and still there. He had smelled it every day of his childhood without noticing it, and now it told him where they were."),
    (18, "Out beyond the bow the haze thinned for a moment. Jake looked where the telescope was pointed and saw it, far off and high, a pale shape against the gray. It was too big to be a bird. Six legs hung beneath it, tucked up like a cat's paws, and the wide flat tail beat the air slowly. He couldn't make out the riders, only a small dark cluster near the head, like spilled pepper."),
    (25, "Then the dark line broke into pieces, and the pieces had masts, and the masts were hung with red. Ship after ship after ship, bow to stern across the whole width of the water, a wall with no gap in it. Black hulls, black smoke curling from the stacks, and on every foredeck a catapult raised against the sky with the fire pots already lit."),
    (29, "\"Enough.\" Iroh stepped up beside him and turned to face him squarely. All the lightness had gone out of his face. \"Zuko. You are still in Earth Kingdom waters. Turn back now and they cannot arrest you. Turn back, and we find another way to your father's good graces, one that does not end with chains. I am begging you.\""),
    (50, "Jake got up. His ears rang with a high, thin note. Men were down all along the deck, some crawling, some not. Through the smoke he made out the aft bulkhead, where planking had split and flames licked up the seam, and beside it a crumpled shape in a crew tunic that wasn't moving."),
    (51, "He ran. Smoke closed over him, bitter and greasy, and he pulled his collar over his mouth and kept going bent double. It was Kaito, on his side with one arm flung out, the hair above his ear singed to a crust. His chest was moving."),
    (62, "The crew swung to it. Men dragged crates away from the fire hand over hand, and Jake went down the line yanking the nearest one by its rope while his palms bled through the leather. Another stone hit the sea close astern, and the ship rang from keel to masthead. Jake lost his footing, caught a rope, and stood up again."),
    (64, "Zuko stood at the rail with his back to the deck. He had not moved. Fire rained across the water on both sides, and he faced it with his shoulders level and his head up, like a man waiting to be let in. Jake could not see his face. He did not need to. He had seen that stance before, in a stone courtyard."),
    (75, "The wall of ships lay all around them, close enough that he could count the rivets on the nearest hull. Their catapults were still raised, and not one was firing. Along the whole line the engines were cutting off one by one, and Fire Nation sailors stood at their rails and watched the burning ship go by. He saw no cheering and heard no shouts. They were only watching."),
    (80, "It rose from the broken stern in a thick black column and bent over in the wind and trailed away across the water behind them, so dark he could see it from anywhere on the ship."),
    (85, "Zuko had come down from the bridge. He stood at the stern rail with the smoke boiling up past him, his armor streaked gray and his hair stuck to his forehead, looking back along the wake. Iroh stood a few paces off. Jake stopped near the mainmast, close enough to hear."),
    (88, "Zuko did not answer at once. His eyes moved along the smoke from the stern to the sky where it fanned out and thinned. Jake saw the change come into his face. It was not relief, and nothing like hope. Something in him had locked into place."),
    (92, "\"In what?\" But Iroh knew. Jake watched him know. His eyes went to the davits on the starboard side, where the small boat hung under a canvas cover, and his mouth eased into something that was not a smile. \"I see.\""),
    (98, "Between them the boat dropped from its slings by degrees and swung once against the hull before it steadied. Smoke rolled over the rail in a black blanket. Jake coughed and kept feeding the rope through his fists, and when the keel kissed the water he let the line run and found that he could not make his hands open. He had to look at them and tell them to."),
    (100, "It was Iroh. He had come up behind them without a sound, which he could do, large as he was. He did not say anything more. He looked at the stained leather, at Jake's face, at Zuko's back as Zuko swung one leg over the rail, and closed one broad hand around Jake's shoulder and held it there, not hard."),
    (110, "He looked over his shoulder once. Zuko sat bolt upright with the tiller line tight around his wrist and his eyes fixed ahead on the haze. The smoke had gotten into his hair and left black streaks along the scar. His back was as straight as a post."),
    (116, "The mist ahead of them was not uniform. A dim bulk showed through it, black against the gray, and as they drew nearer it rose out of the haze one piece at a time. First a long curve of dark shore, shaped like a drawn bow. Then a cliff above it, and above the cliff a mountain with its upper slopes gone red where the light struck them from behind."),
    (117, "And on the mountain's shoulder, tier above tier, stood a temple. Its roofs rose in sweeping red-and-gold eaves, one over another, each layer narrower than the last, as if a building were trying to climb the sky. Bronze doors glinted at its base. From this far it looked as quiet as a painting."),
    (119, "He knew buildings like this. He had walked past their cousins in the palace gardens as a boy, scrubbing the steps with a rag while the sages in their robes went by without noticing him. He knew the incense, the deep brass gongs, and the cold flagstones under his knees."),
    (122, "The shore came up fast. The water went from glass to black stone, a rim of jagged volcanic rock heaped in broken plates along the waterline, rough as old slag. The boat slid in on a long slow swell. Jake shipped the oars, braced his boots, and felt the hull grind onto the rock with a groan that carried a long way over the silent water."),
    (133, "It was an old, familiar weight. The sheath lay flat against his hip, and the grip's linen wrapping lay against the cut in his right palm like a nail. He tightened his fingers on the hilt anyway, and in the dark he counted his heartbeats because there was nothing else to count."),
    (149, "\"It was a noble effort, Prince Zuko,\" Zhao said. His voice carried perfectly in the great chamber. It was warm and rich, and pleased. \"But your little smokescreen didn't work.\""),
    (157, "\"You're too late, Zhao!\" Zuko said. His voice was raw, but it did not shake. He lifted his chin and stared up at the commander with the left side of his face burning in the torchlight. \"The Avatar's inside, and the doors are sealed.\""),
    (177, "Then the wave took them, all of them, and flung them backward across the black floor like leaves. A man in red-lacquered armor went past the gallery rail at head height and struck the far wall. Zhao's plume was gone. He was on his back on the stone, one arm across his face, his cloak smoking."),
    (190, "They ran. The corridors that had been silent half an hour ago were alive with noise: the roar of the mountain, the screech of tearing timber, the crash of falling stone. Lamps swung from their brackets and went out. Walls leaned. Jake ran with his arm clamped against his chest and his boots skidding on the hot flagstones. Zuko ran beside him, keeping pace, one hand always an inch from Jake's sleeve."),
    (199, "Then he hauled the free tail across the steel with both arms from the shoulder, like someone emptying a net. Something in the rope gave with a creak, and the line sighed down along the beam and hung free over the glow. The motion had cost him nothing in the fingers and everything in the palm; the leather went hot, and a wet line ran down inside the right sleeve."),
    (219, "A shape was climbing out of the glow above the island. It was huge and white and shaggy, with a broad flat tail and six legs tucked beneath it, rising steadily on the hot air with a slow, powerful beat. It crossed the red face of the mountain and entered the dark. On its back, for a moment, Jake saw a few small shapes huddled together, tiny against the sky. Then the stars took it."),
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
