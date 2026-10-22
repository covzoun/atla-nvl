#!/usr/bin/env python3
"""Chapter 9 coda trim: the Katara interlude (paragraph 268 onward).

Runs after tools/trim_ch9_body.py. Paragraphs are located by their opening
text rather than by a hard index, so the script survives a re-run of the body
trim. Each entry is (expected_prefix, new_text); the prefix assertion catches
an off-by-one immediately.
"""
import io
import sys

PATH = "chapters/Chapter_09.md"

# (expected_prefix, new_text) -- prefix must match the start of the paragraph.
CODA = [
    ("The wind off the gorge",
     "The wind off the gorge had a bite in it, and Katara pulled the fur collar of her parka up around her ears."),
    ("Appa flew steadily.",
     "Sky and cloud and the tops of far hills slid by on either side. Behind them the roar of the falls had dwindled to a murmur and then to nothing. On Appa's neck Aang sat cross-legged with the reins loose in his hands."),
    ("She had been rehearsing it since the pirate ship.",
     "She had been rehearsing it since the pirate ship. She moved forward along the saddle until she was close enough to touch his shoulder."),
    ("\"I'm sorry. About the scroll.",
     "\"I'm sorry. About the scroll.\" She made herself keep looking at him. \"I was jealous. You were picking it up so fast, and I was the one who wanted it so badly, so I said other things instead. Things I shouldn't have. You didn't deserve it.\""),
    ("Aang's face went through three or four expressions",
     "Aang's face went through several expressions in a row and settled on the open one."),
    ("\"Maybe a little.\"",
     "\"Maybe a little.\" He grinned. \"But you came back for me. That counts for more.\""),
    ("She laughed, a little shakily,",
     "She laughed, a little shakily, and put her arm around his shoulders."),
    ("He was sprawled at the back of the saddle",
     "He had been very quiet for a while. Now he sat up."),
    ("Katara stared at it.",
     "Katara stared at it. Then she was across the saddle with both hands out."),
    ("\"Skill. Stealth. Unbelievable grace.\"",
     "\"Skill. Stealth. Unbelievable grace.\" \"I'm still waiting for a thank-you, by the way.\""),
    ("She was holding it.",
     "The parchment was dry and fragile. The painted figures down its length had not been touched. She turned it toward the light and saw a woman with her hands raised and a ribbon of water between them."),
    ("Aang laughed, and Appa let out",
     "Aang laughed."),
    ("Then Katara looked down at the scroll in her hands,",
     "Then Katara looked down at the scroll, and her mind slid away."),
    ("She could see it as plainly as",
     "Brown water, black mud, the white-hot flash of Zuko's fire on the shore. And in a gap in the smoke, a boy."),
    ("\"Him.\" Her voice came out smaller",
     "\"Him.\" \"On the shore. At the end.\""),
    ("\"Zuko?\" Sokka said.",
     "\"Zuko?\" Sokka said. \"I saw him ruin a perfectly good escape by shouting about his boat.\""),
    ("Neither of them said anything.",
     "Neither of them said anything. Aang had turned all the way around on Appa's neck. Sokka frowned."),
    ("\"There was a boy,\" Katara said.",
     "\"There was a boy,\" Katara said. \"A little taller than me. Dark hair. A dark coat with red lining. He was standing right behind Zuko, and he had...\" \"He was bending, Sokka.\""),
    ("The wind went past them in a long thin note.",
     "The wind went past them in a long thin note. Sokka sat up straighter."),
    ("\"A waterbender.\" He said the word",
     "\"A waterbender.\" \"Working for the Fire Nation. We left the South Pole because there weren't any waterbenders left. You're the last one. That's why we're going north, to find a master. That's the plan.\""),
    ("\"So there's no way there's some other waterbender",
     "\"So there's no way there's some other waterbender.\""),
    ("It came out harder than she had intended,",
     "It came out harder than she had intended, and Sokka's mouth shut. She looked down at her own hands and could not seem to stop."),
    ("\"I watched him,\" she said.",
     "\"I watched him,\" she said. \"The whole time I was pushing the ship out. I looked back, and there he was. He pulled a whole stream off the shallows with his hands and he didn't swing it. It went in straight lines. Like a whip. Like...\" \"Like a fire strike. He had his feet together, almost, and his arms were so tight. Everything was sharp. It didn't *flow.*\""),
    ("\"No. He's good.\"",
     "\"No. He's good.\" \"That's what's wrong. He was really good. And it didn't look like anything I've ever seen.\""),
    ("Aang had been very still.",
     "Aang had been very still. \"Maybe someone taught him,\" he said. \"Somewhere else.\""),
    ("\"Who?\" said Katara.",
     "\"Who?\" said Katara. \"Who would teach him?\" \"I'm the only waterbender I know, Sokka. That's why we're going north.\" \"And then I look up and there's another one right there, close to my age, standing next to the one person who...\""),
    ("\"He was on the *other side,*\" said Sokka",
     "\"He was on the *other side,*\" said Sokka. \"Now he's got a waterbender on his team. Which is great. That's great. I love this.\""),
    ("\"I know. But he looked...\"",
     "\"I know. But he looked...\" \"I don't know. Did he look scared to you?\""),
    ("\"I don't know what he looked like,\" Katara said.",
     "\"I don't know what he looked like,\" Katara said. She did. She had seen his face for three heartbeats through a rip in the smoke, and it was fixed in her head like a carving. A pale, tired face, soft in the jaw, and eyes that were a color she could not have named from that distance. He had not looked triumphant. For a moment he had looked, of all the things she could have imagined, caught."),
    ("His hands had been wrapped.",
     "His hands had been wrapped. Under the gloves, ragged ones, something had been wrong with them, and the water had circled in and out of his fingers and not once had he flinched."),
    ("She touched her own hands.",
     "She touched her own hands. They still remembered the shape of a stream pulled through the air, and she tried to make them move the way his had. Straight, short, hard. The water in her mind went the wrong way. It did not want to be held like that."),
    ("Her fingers drifted to her throat",
     "Her fingers drifted to her throat and found nothing. The place where her mother's necklace had hung was bare skin."),
    ("Katara looked down at the scroll in her lap.",
     "Katara looked down at the scroll in her lap. The figure of the woman on it stared up at her with her hands lifted and the water curling between them."),
    ("She knew what that kind of bending looked like.",
     "She knew what that kind of bending looked like. It did not look like a boy in a Fire Nation coat with his feet set apart and every line of him drawn tight as a bowstring."),
    ("Appa banked gently,",
     "Appa banked gently, and the sun swung across the saddle. The wind was cold on her face. She held the scroll against her chest."),
]


def main():
    text = io.open(PATH, encoding="utf-8").read()
    ps = text.split("\n\n")
    before = len(text.split())

    for prefix, new in CODA:
        hits = [i for i, p in enumerate(ps) if p.startswith(prefix)]
        if len(hits) != 1:
            sys.exit("prefix %r matched %d paragraphs" % (prefix, len(hits)))
        ps[hits[0]] = new

    out = "\n\n".join(ps)

    # The coda opens with a scene break and an italic location line, matching
    # the Ch 1 / 4 / 5 / 10 interludes. Rebuild the header idempotently.
    marker = "*Above the river valley, late afternoon.*"
    if marker in out:
        out = out.replace("---\n\n" + marker, marker)
    head, sep, tail = out.partition("The wind off the gorge had a bite in it")
    if not sep:
        sys.exit("coda opener not found")
    out = head + "---\n\n" + marker + "\n\nThe wind off the gorge had a bite in it" + tail

    io.open(PATH, "w", encoding="utf-8").write(out)
    print("words %d -> %d" % (before, len(out.split())))


if __name__ == "__main__":
    main()
