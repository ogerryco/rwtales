#!/usr/bin/env python3
"""Audita protagonistas, menciones y rendimiento por artista/banda en TikTok."""

from __future__ import annotations

import argparse
import csv
import json
import re
import statistics
import unicodedata
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


# El nombre canónico se mantiene separado de sus proyectos. La columna ecosystem
# permite sumar la franquicia sin confundir a una persona con una banda.
ENTITIES = [
    # Seattle / alternative
    ("Chris Cornell", "artist", "Cornell", ["chris cornell", "chriscornell"]),
    ("Soundgarden", "band", "Cornell", ["soundgarden"]),
    ("Audioslave", "band", "Cornell", ["audioslave"]),
    ("Temple of the Dog", "band", "Cornell", ["temple of the dog", "templeofthedog"]),
    ("Scott Weiland", "artist", "Weiland", ["scott weiland", "scottweiland", "weiland"]),
    ("Stone Temple Pilots", "band", "Weiland", ["stone temple pilots", "stonetemplepilots", "stone tempel pilots", "stonetempelpilots", "stp"]),
    ("Velvet Revolver", "band", "Weiland", ["velvet revolver", "velvetrevolver"]),
    ("Pearl Jam", "band", "Pearl Jam", ["pearl jam", "pearljam"]),
    ("Eddie Vedder", "artist", "Pearl Jam", ["eddie vedder", "eddievedder"]),
    ("Mike McCready", "artist", "Pearl Jam", ["mike mccready", "mikemccready"]),
    ("Jeff Ament", "artist", "Pearl Jam", ["jeff ament", "jeffament"]),
    ("Mother Love Bone", "band", "Pearl Jam", ["mother love bone", "motherlovebone"]),
    ("Andrew Wood", "artist", "Pearl Jam", ["andrew wood", "andrewwood"]),
    ("Alice in Chains", "band", "Alice in Chains", ["alice in chains", "aliceinchains"]),
    ("Layne Staley", "artist", "Alice in Chains", ["layne staley", "laynestaley"]),
    ("Jerry Cantrell", "artist", "Alice in Chains", ["jerry cantrell", "jerrycantrell"]),
    ("Mad Season", "band", "Alice in Chains", ["mad season", "madseason"]),
    ("Nirvana", "band", "Nirvana", ["nirvana"]),
    ("Kurt Cobain", "artist", "Nirvana", ["kurt cobain", "kurtcobain"]),
    ("Dave Grohl", "artist", "Grohl/Foo Fighters", ["dave grohl", "davegrohl"]),
    ("Foo Fighters", "band", "Grohl/Foo Fighters", ["foo fighters", "foofighters"]),
    ("Matt Cameron", "artist", "Seattle", ["matt cameron", "mattcameron"]),
    ("Blind Melon", "band", "Blind Melon", ["blind melon", "blindmelon"]),
    ("Candlebox", "band", "Candlebox", ["candlebox"]),
    # Classic rock / metal
    ("Led Zeppelin", "band", "Led Zeppelin", ["led zeppelin", "ledzeppelin"]),
    ("Jimmy Page", "artist", "Led Zeppelin", ["jimmy page", "jimmypage"]),
    ("Robert Plant", "artist", "Led Zeppelin", ["robert plant", "robertplant"]),
    ("John Bonham", "artist", "Led Zeppelin", ["john bonham", "johnbonham"]),
    ("Pink Floyd", "band", "Pink Floyd", ["pink floyd", "pinkfloyd"]),
    ("David Gilmour", "artist", "Pink Floyd", ["david gilmour", "davidgilmour"]),
    ("Roger Waters", "artist", "Pink Floyd", ["roger waters", "rogerwaters"]),
    ("Syd Barrett", "artist", "Pink Floyd", ["syd barrett", "sydbarrett"]),
    ("The Beatles", "band", "Beatles", ["the beatles", "thebeatles", "beatles"]),
    ("John Lennon", "artist", "Beatles", ["john lennon", "johnlennon"]),
    ("Paul McCartney", "artist", "Beatles", ["paul mccartney", "paulmccartney"]),
    ("George Harrison", "artist", "Beatles", ["george harrison", "georgeharrison"]),
    ("Ringo Starr", "artist", "Beatles", ["ringo starr", "ringostarr"]),
    ("The Rolling Stones", "band", "Rolling Stones", ["rolling stones", "rollingstones"]),
    ("Mick Jagger", "artist", "Rolling Stones", ["mick jagger", "mickjagger"]),
    ("Keith Richards", "artist", "Rolling Stones", ["keith richards", "keithrichards"]),
    ("Queen", "band", "Queen", ["queen"]),
    ("Brian May", "artist", "Queen", ["brian may", "brianmay"]),
    ("Black Sabbath", "band", "Black Sabbath/Ozzy", ["black sabbath", "blacksabbath"]),
    ("Ozzy Osbourne", "artist", "Black Sabbath/Ozzy", ["ozzy osbourne", "ozzyosbourne", "ozzy"]),
    ("Metallica", "band", "Metallica", ["metallica"]),
    ("James Hetfield", "artist", "Metallica", ["james hetfield", "jameshetfield", "hetfield"]),
    ("AC/DC", "band", "AC/DC", ["ac dc", "acdc"]),
    ("Bon Scott", "artist", "AC/DC", ["bon scott", "bonscott"]),
    ("Brian Johnson", "artist", "AC/DC", ["brian johnson", "brianjohnson"]),
    ("Van Halen", "band", "Van Halen", ["van halen", "vanhalen"]),
    ("Eddie Van Halen", "artist", "Van Halen", ["eddie van halen", "eddievanhalen"]),
    ("Sammy Hagar", "artist", "Van Halen", ["sammy hagar", "sammyhagar"]),
    ("Aerosmith", "band", "Aerosmith", ["aerosmith"]),
    ("Steven Tyler", "artist", "Aerosmith", ["steven tyler", "steventyler"]),
    ("Joe Perry", "artist", "Aerosmith", ["joe perry", "joeperry"]),
    ("Guns N' Roses", "band", "Guns N' Roses", ["guns n roses", "gunsnroses", "gnr"]),
    ("Axl Rose", "artist", "Guns N' Roses", ["axl rose", "axlrose"]),
    ("Slash", "artist", "Guns N' Roses", ["slash"]),
    ("Duff McKagan", "artist", "Guns N' Roses", ["duff mckagan", "duffmckagan"]),
    ("Def Leppard", "band", "Def Leppard", ["def leppard", "defleppard"]),
    ("Iron Maiden", "band", "Iron Maiden", ["iron maiden", "ironmaiden"]),
    ("Deep Purple", "band", "Deep Purple", ["deep purple", "deeppurple"]),
    ("Kiss", "band", "Kiss", ["kiss"]),
    ("Paul Stanley", "artist", "Kiss", ["paul stanley", "paulstanley"]),
    ("Gene Simmons", "artist", "Kiss", ["gene simmons", "genesimmons"]),
    ("Skid Row", "band", "Skid Row", ["skid row", "skidrow"]),
    ("Sebastian Bach", "artist", "Skid Row", ["sebastian bach", "sebastianbach"]),
    ("Poison", "band", "Poison", ["poison"]),
    ("Bret Michaels", "artist", "Poison", ["bret michaels", "bretmichaels"]),
    ("Bon Jovi", "band", "Bon Jovi", ["bon jovi", "bonjovi"]),
    ("Jon Bon Jovi", "artist", "Bon Jovi", ["jon bon jovi", "jonbonjovi"]),
    ("Journey", "band", "Journey", ["journey"]),
    ("Steve Perry", "artist", "Journey", ["steve perry", "steveperry"]),
    ("Foreigner", "band", "Foreigner", ["foreigner"]),
    ("The Eagles", "band", "Eagles", ["the eagles", "theeagles", "eagles"]),
    ("Fleetwood Mac", "band", "Fleetwood Mac", ["fleetwood mac", "fleetwoodmac"]),
    ("Stevie Nicks", "artist", "Fleetwood Mac", ["stevie nicks", "stevienicks"]),
    ("The Doors", "band", "The Doors", ["the doors", "thedoors"]),
    ("Jim Morrison", "artist", "The Doors", ["jim morrison", "jimmorrison"]),
    ("The Cars", "band", "The Cars", ["the cars", "thecars"]),
    ("Ric Ocasek", "artist", "The Cars", ["ric ocasek", "ricocasek"]),
    # Alternative / 80s / 90s / 2000s
    ("Red Hot Chili Peppers", "band", "RHCP", ["red hot chili peppers", "redhotchilipeppers", "rhcp"]),
    ("John Frusciante", "artist", "RHCP", ["john frusciante", "johnfrusciante", "frusciante"]),
    ("Flea", "artist", "RHCP", ["flea"]),
    ("Chad Smith", "artist", "RHCP", ["chad smith", "chadsmith"]),
    ("Hillel Slovak", "artist", "RHCP", ["hillel slovak", "hillelslovak"]),
    ("Linkin Park", "band", "Linkin Park", ["linkin park", "linkinpark"]),
    ("Chester Bennington", "artist", "Linkin Park", ["chester bennington", "chesterbennington"]),
    ("Mike Shinoda", "artist", "Linkin Park", ["mike shinoda", "mikeshinoda", "shinoda"]),
    ("Emily Armstrong", "artist", "Linkin Park", ["emily armstrong", "emilyarmstrong"]),
    ("Radiohead", "band", "Radiohead", ["radiohead"]),
    ("Thom Yorke", "artist", "Radiohead", ["thom yorke", "thomyorke"]),
    ("Nine Inch Nails", "band", "Nine Inch Nails", ["nine inch nails", "nineinchnails", "nin"]),
    ("Trent Reznor", "artist", "Nine Inch Nails", ["trent reznor", "trentreznor"]),
    ("The Smashing Pumpkins", "band", "Smashing Pumpkins", ["smashing pumpkins", "smashingpumpkins"]),
    ("Billy Corgan", "artist", "Smashing Pumpkins", ["billy corgan", "billycorgan"]),
    ("The Cure", "band", "The Cure", ["the cure", "thecure"]),
    ("Robert Smith", "artist", "The Cure", ["robert smith", "robertsmith"]),
    ("Depeche Mode", "band", "Depeche Mode", ["depeche mode", "depechemode"]),
    ("Dave Gahan", "artist", "Depeche Mode", ["dave gahan", "davegahan"]),
    ("Martin Gore", "artist", "Depeche Mode", ["martin gore", "martingore"]),
    ("Oasis", "band", "Oasis", ["oasis"]),
    ("Noel Gallagher", "artist", "Oasis", ["noel gallagher", "noelgallagher"]),
    ("Liam Gallagher", "artist", "Oasis", ["liam gallagher", "liamgallagher"]),
    ("The Black Crowes", "band", "Black Crowes", ["the black crowes", "theblackcrowes"]),
    ("Collective Soul", "band", "Collective Soul", ["collective soul", "collectivesoul"]),
    ("Ed Roland", "artist", "Collective Soul", ["ed roland", "edroland"]),
    ("Counting Crows", "band", "Counting Crows", ["counting crows", "countingcrows"]),
    ("Adam Duritz", "artist", "Counting Crows", ["adam duritz", "adamduritz"]),
    ("Green Day", "band", "Green Day", ["green day", "greenday"]),
    ("Jane's Addiction", "band", "Jane's Addiction", ["jane s addiction", "janesaddiction"]),
    ("Perry Farrell", "artist", "Jane's Addiction", ["perry farrell", "perryfarrell"]),
    ("Placebo", "band", "Placebo", ["placebo"]),
    ("Brian Molko", "artist", "Placebo", ["brian molko", "brianmolko"]),
    ("Garbage", "band", "Garbage", ["garbage"]),
    ("Shirley Manson", "artist", "Garbage", ["shirley manson", "shirleymanson"]),
    ("INXS", "band", "INXS", ["inxs"]),
    ("Michael Hutchence", "artist", "INXS", ["michael hutchence", "michaelhutchence"]),
    ("Kings of Leon", "band", "Kings of Leon", ["kings of leon", "kingsofleon"]),
    ("Greta Van Fleet", "band", "Greta Van Fleet", ["greta van fleet", "gretavanfleet"]),
    ("The Warning", "band", "The Warning", ["the warning", "thewarning"]),
    ("U2", "band", "U2", ["u2"]),
    ("Snow Patrol", "band", "Snow Patrol", ["snow patrol", "snowpatrol"]),
    # Latin / solo / adjacent
    ("Gustavo Cerati", "artist", "Cerati/Soda", ["gustavo cerati", "gustavocerati", "cerati"]),
    ("Soda Stereo", "band", "Cerati/Soda", ["soda stereo", "sodastereo"]),
    ("Enrique Bunbury", "artist", "Héroes/Bunbury", ["enrique bunbury", "bunbury"]),
    ("Héroes del Silencio", "band", "Héroes/Bunbury", ["heroes del silencio", "héroes del silencio", "heroesdelsilencio"]),
    ("Jarabe de Palo", "band", "Jarabe de Palo", ["jarabe de palo", "jarabedepalo"]),
    ("David Bowie", "artist", "David Bowie", ["david bowie", "davidbowie"]),
    ("Prince", "artist", "Prince", ["prince"]),
    ("Michael Jackson", "artist", "Michael Jackson", ["michael jackson", "michaeljackson"]),
    ("George Michael", "artist", "George Michael", ["george michael", "georgemichael"]),
    ("Elton John", "artist", "Elton John", ["elton john", "eltonjohn"]),
    ("Sting", "artist", "Sting", ["sting"]),
    ("Rod Stewart", "artist", "Rod Stewart", ["rod stewart", "rodstewart"]),
    ("Phil Collins", "artist", "Phil Collins", ["phil collins", "philcollins"]),
    ("Christopher Cross", "artist", "Christopher Cross", ["christopher cross", "christophercross"]),
    ("Lenny Kravitz", "artist", "Lenny Kravitz", ["lenny kravitz", "lennykravitz"]),
    ("Carlos Santana", "artist", "Santana", ["carlos santana", "carlossantana", "santana"]),
    ("Jack White", "artist", "Jack White", ["jack white", "jackwhite"]),
    ("Marilyn Manson", "artist", "Marilyn Manson", ["marilyn manson", "marilynmanson"]),
    ("Jimi Hendrix", "artist", "Jimi Hendrix", ["jimi hendrix", "jimihendrix"]),
    ("Eric Clapton", "artist", "Eric Clapton", ["eric clapton", "ericclapton"]),
    ("Jeff Beck", "artist", "Jeff Beck", ["jeff beck", "jeffbeck"]),
    ("Joe Satriani", "artist", "Joe Satriani", ["joe satriani", "joesatriani"]),
    ("Steve Vai", "artist", "Steve Vai", ["steve vai", "stevevai"]),
    ("Peter Frampton", "artist", "Peter Frampton", ["peter frampton", "peterframpton"]),
    ("Bob Dylan", "artist", "Bob Dylan", ["bob dylan", "bobdylan"]),
    ("Elvis Presley", "artist", "Elvis Presley", ["elvis presley", "elvispresley"]),
    ("Björk", "artist", "Björk", ["bjork", "björk"]),
    ("Toni Cornell", "artist", "Cornell", ["toni cornell", "tonicornell"]),
    # Long tail presente en el catálogo
    ("Alice Cooper", "artist", "Alice Cooper", ["alice cooper", "alicecooper"]),
    ("Kid Rock", "artist", "Kid Rock", ["kid rock", "kidrock"]),
    ("Annie Lennox", "artist", "Eurythmics", ["annie lennox", "annielennox"]),
    ("Eurythmics", "band", "Eurythmics", ["eurythmics"]),
    ("Lana Del Rey", "artist", "Lana Del Rey", ["lana del rey", "lanadelrey"]),
    ("Mr. Mister", "band", "Mr. Mister", ["mr mister", "mrmister"]),
    ("Billy Gibbons", "artist", "ZZ Top", ["billy gibbons", "billy f gibbons", "billyfgibbons"]),
    ("ZZ Top", "band", "ZZ Top", ["zz top", "zztop"]),
    ("Fito Páez", "artist", "Fito Páez", ["fito paez", "fitopaez"]),
    ("Mark Knopfler", "artist", "Dire Straits", ["mark knopfler", "markknopfler"]),
    ("Dire Straits", "band", "Dire Straits", ["dire straits", "direstraits"]),
    ("Crowded House", "band", "Crowded House", ["crowded house", "crowdedhouse"]),
    ("Pantera", "band", "Pantera", ["pantera"]),
    ("Rex Brown", "artist", "Pantera", ["rex brown", "rexbrown"]),
    ("Jewel", "artist", "Jewel", ["jewel"]),
    ("Rita Guerrero", "artist", "Santa Sabina", ["rita guerrero", "ritaguerrero"]),
    ("Santa Sabina", "band", "Santa Sabina", ["santa sabina", "santasabina"]),
    ("Janis Joplin", "artist", "Janis Joplin", ["janis joplin", "janisjoplin"]),
    ("Dorothy", "band", "Dorothy", ["dorothy martin", "dorothymartin", "banda dorothy"]),
    ("Robbie Williams", "artist", "Robbie Williams", ["robbie williams", "robbiewilliams"]),
    ("Maroon 5", "band", "Maroon 5", ["maroon 5", "maroon5"]),
    ("Muse", "band", "Muse", ["muse"]),
    ("Julian Casablancas", "artist", "The Strokes", ["julian casablancas", "juliancasablancas"]),
    ("The Strokes", "band", "The Strokes", ["the strokes", "thestrokes"]),
    ("Lita Ford", "artist", "Lita Ford", ["lita ford", "litaford"]),
    ("Dave Matthews", "artist", "Dave Matthews Band", ["dave matthews", "davematthews"]),
    ("Dave Matthews Band", "band", "Dave Matthews Band", ["dave matthews band", "davematthewsband"]),
    ("Tool", "band", "Tool", ["tool band", "toolband", "tool"]),
    ("Maynard James Keenan", "artist", "Tool", ["maynard james keenan", "maynardjameskeenan"]),
    ("Twisted Sister", "band", "Twisted Sister", ["twisted sister", "twistedsister"]),
    ("Dee Snider", "artist", "Twisted Sister", ["dee snider", "deesnider"]),
    ("James", "band", "James", ["james laid"]),
    ("The Beach Boys", "band", "Beach Boys", ["the beach boys", "thebeachboys", "beach boys"]),
    ("Brian Wilson", "artist", "Beach Boys", ["brian wilson", "brianwilson"]),
    ("Thirty Seconds to Mars", "band", "Thirty Seconds to Mars", ["thirty seconds to mars", "thirtysecondstomars"]),
    ("Pat Benatar", "artist", "Pat Benatar", ["pat benatar", "patbenatar"]),
    ("Faith No More", "band", "Faith No More", ["faith no more", "faithnomore"]),
    ("Mike Patton", "artist", "Faith No More", ["mike patton", "mikepatton"]),
    ("Korn", "band", "Korn", ["korn"]),
    ("Tears for Fears", "band", "Tears for Fears", ["tears for fears", "tearsforfears"]),
    ("Fiona Apple", "artist", "Fiona Apple", ["fiona apple", "fionaapple"]),
    ("Delta Spirit", "band", "Delta Spirit", ["delta spirit", "deltaspirit"]),
    ("Alanis Morissette", "artist", "Alanis Morissette", ["alanis morissette", "alanis"]),
    ("Underworld", "band", "Underworld", ["underworld"]),
    ("Boy George", "artist", "Culture Club", ["boy george", "boygeorge"]),
    ("Culture Club", "band", "Culture Club", ["culture club", "cultureclub"]),
    ("Chris de Burgh", "artist", "Chris de Burgh", ["chris de burgh", "chrisdeburgh"]),
    ("Mudhoney", "band", "Mudhoney", ["mudhoney"]),
    ("Goo Goo Dolls", "band", "Goo Goo Dolls", ["goo goo dolls", "googoodolls"]),
    ("John Rzeznik", "artist", "Goo Goo Dolls", ["john rzeznik", "johnrzeznik"]),
    ("Creed", "band", "Creed", ["creed"]),
    ("Cutting Crew", "band", "Cutting Crew", ["cutting crew", "cuttingcrew"]),
    ("Nick Van Eede", "artist", "Cutting Crew", ["nick van eede", "nickvaneede"]),
    ("Megadeth", "band", "Megadeth", ["megadeth"]),
    ("Dave Mustaine", "artist", "Megadeth", ["dave mustaine", "davemustaine"]),
    ("Live", "band", "Live", ["lighting crashes", "live band"]),
    ("Mazzy Star", "band", "Mazzy Star", ["mazzy star", "mazzystar"]),
    ("Mr. Big", "band", "Mr. Big", ["mr big", "mrbig"]),
    ("Eric Martin", "artist", "Mr. Big", ["eric martin", "ericmartin"]),
    ("Ugly Kid Joe", "band", "Ugly Kid Joe", ["ugly kid joe", "uglykidjoe"]),
    ("Massive Attack", "band", "Massive Attack", ["massive attack", "massiveattack"]),
    ("GusGus", "band", "GusGus", ["gus gus", "gusgus"]),
    ("Cigarettes After Sex", "band", "Cigarettes After Sex", ["cigarettes after sex", "cigarettesaftersex"]),
    ("Night Traveler", "band", "Night Traveler", ["night traveler", "nighttraveler", "nightraveller"]),
    ("The Big Push", "band", "The Big Push", ["the big push", "thebigpush"]),
    ("REO Speedwagon", "band", "REO Speedwagon", ["reo speedwagon", "reospeedwagon"]),
    ("Kevin Cronin", "artist", "REO Speedwagon", ["kevin cronin", "kevincronin"]),
    ("IDLES", "band", "IDLES", ["idles"]),
    ("Brian Eno", "artist", "Brian Eno", ["brian eno", "brianeno"]),
    ("Duncan Sheik", "artist", "Duncan Sheik", ["duncan sheik", "duncansheik"]),
    ("Chickenfoot", "band", "Chickenfoot", ["chickenfoot"]),
    ("Travis", "band", "Travis", ["travis sing", "travis band"]),
    ("Sade", "artist", "Sade", ["sade"]),
    ("When in Rome", "band", "When in Rome", ["when in rome", "wheninrome"]),
    ("The Cranberries", "band", "The Cranberries", ["the cranberries", "thecranberries", "cranberries"]),
    ("Dolores O'Riordan", "artist", "The Cranberries", ["dolores o riordan", "doloresoriordan"]),
    ("Keane", "band", "Keane", ["keane"]),
    ("Blur", "band", "Blur", ["blur"]),
    ("The Verve", "band", "The Verve", ["the verve", "theverve"]),
    ("Coldplay", "band", "Coldplay", ["coldplay"]),
    ("Portishead", "band", "Portishead", ["portishead"]),
    ("Sheryl Crow", "artist", "Sheryl Crow", ["sheryl crow", "sheryl crowl", "sherylcrow"]),
    ("Glenn Frey", "artist", "Eagles", ["glenn frey", "glennfrey"]),
    ("Pink", "artist", "Pink", ["pink stern"]),
    ("Rammstein", "band", "Rammstein", ["rammstein"]),
    ("HAEVN", "band", "HAEVN", ["haevn"]),
    ("Train", "band", "Train", ["train band", "soul vacation"]),
    ("EMF", "band", "EMF", ["emf"]),
    ("Natalie Imbruglia", "artist", "Natalie Imbruglia", ["natalie imbruglia", "natalieimbruglia"]),
    ("Hot Chip", "band", "Hot Chip", ["hot chip", "hotchip"]),
    ("Daniel Caesar", "artist", "Daniel Caesar", ["daniel caesar", "danielcaesar"]),
    ("Jeff Buckley", "artist", "Jeff Buckley", ["jeff buckley", "jeffbuckley"]),
    ("Taylor Hawkins", "artist", "Grohl/Foo Fighters", ["taylor hawkins", "taylorhawkins"]),
    ("Tom Petty", "artist", "Tom Petty", ["tom petty", "tompetty"]),
]

ANGLE_RULES = {
    "entrevista/confesión": r"\bentrevista|confes|habl[oó]|revel[oó]|dijo|pregunta\b",
    "muerte/adversidad": r"\bmuri[oó]|muerte|fallec|adicci|depresi|suicid|traged|demonios|dolor\b",
    "presentación/canción": r"\ben vivo|concierto|interpret|cant[oó]|toc[oó]|versi[oó]n|canci[oó]n|performance|lollapalooza\b",
    "conflicto/negocio": r"\bexpuls|demand|millones|dinero|pelea|rechaz|despid|corrieron|industria|contrato\b",
    "familia/relación": r"\bhij[oa]|padre|madre|espos|viud|familia|amor|pareja\b",
    "historia/legado": r"\bhistoria|legado|origen|aniversario|carrera|biograf|recordamos|hall of fame\b",
    "noticia/actualidad": r"\b2025|2026|regres[oó]|volvi[oó]|nuevo|anunci|noticia|festival\b",
    "instrumento/técnica": r"\bguitarra|riff|solo|voz|bater[ií]a|t[eé]cnica|sonido|producci[oó]n\b",
}


def norm(value: str) -> str:
    value = unicodedata.normalize("NFKD", value or "")
    value = "".join(c for c in value if not unicodedata.combining(c)).casefold()
    return re.sub(r"[^a-z0-9]+", " ", value).strip()


def median(values):
    return statistics.median(values) if values else 0


def percentile(values, q):
    if not values:
        return 0
    ordered = sorted(values)
    index = (len(ordered) - 1) * q
    lo, hi = int(index), min(int(index) + 1, len(ordered) - 1)
    return ordered[lo] + (ordered[hi] - ordered[lo]) * (index - lo)


def alias_pos(text: str, aliases: list[str]) -> int | None:
    positions = []
    for alias in aliases:
        match = re.search(rf"(?<![a-z0-9]){re.escape(norm(alias))}(?![a-z0-9])", text)
        if match:
            positions.append(match.start())
    return min(positions) if positions else None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--catalog", type=Path, required=True)
    parser.add_argument("--csv", type=Path, required=True)
    parser.add_argument("--json", type=Path, required=True)
    parser.add_argument("--as-of", default="2026-07-26")
    parser.add_argument("--recent-days", type=int, default=90)
    args = parser.parse_args()

    payload = json.loads(args.catalog.read_text(encoding="utf-8"))
    videos = payload["videos"] if isinstance(payload, dict) else payload
    entities = [
        {"name": n, "type": t, "ecosystem": e, "aliases": a}
        for n, t, e, a in ENTITIES
    ]
    as_of = datetime.fromisoformat(args.as_of).replace(tzinfo=timezone.utc)
    cutoff = args.recent_days * 86400
    rows = []
    unmatched = []

    for video in videos:
        raw = video.get("video_description") or video.get("title", "")
        text = norm(raw)
        prehash = norm(raw.split("#", 1)[0])
        tags = [norm(x) for x in re.findall(r"#([\wáéíóúüñÁÉÍÓÚÜÑ]+)", raw)]
        matches = []
        for entity in entities:
            p_all = alias_pos(text, entity["aliases"])
            if p_all is None:
                continue
            p_pre = alias_pos(prehash, entity["aliases"])
            tag_hit = any(norm(a).replace(" ", "") in {t.replace(" ", "") for t in tags} for a in entity["aliases"])
            score = 1
            if tag_hit:
                score += 2
            if p_pre is not None:
                score += 4
                if p_pre < 180:
                    score += 5
            matches.append((score, p_all, entity))

        created = datetime.fromtimestamp(int(video.get("create_time", 0)), tz=timezone.utc)
        base = {
            "id": str(video.get("id", "")),
            "date": created.date().isoformat(),
            "recent": 0 <= (as_of - created).total_seconds() <= cutoff,
            "views": int(video.get("view_count", 0)),
            "likes": int(video.get("like_count", 0)),
            "comments": int(video.get("comment_count", 0)),
            "shares": int(video.get("share_count", 0)),
            "duration": int(video.get("duration", 0)),
            "title": raw,
        }
        if matches:
            matches.sort(key=lambda item: (-item[0], item[1], item[2]["name"]))
            lead = matches[0][2]
            base["primary"] = lead["name"]
            base["mentions"] = [m[2]["name"] for m in matches]
        else:
            base["primary"] = ""
            base["mentions"] = []
            unmatched.append(base)
        rows.append(base)

    all_views = [r["views"] for r in rows]
    channel_median = median(all_views)
    top_cutoff = percentile(all_views, 0.90)
    output = []
    for entity in entities:
        primary = [r for r in rows if r["primary"] == entity["name"]]
        mentions = [r for r in rows if entity["name"] in r["mentions"]]
        if not mentions:
            continue
        recent_primary = [r for r in primary if r["recent"]]
        historical_primary = [r for r in primary if not r["recent"]]
        angle_counts = Counter()
        for r in primary:
            matched_angles = [name for name, rule in ANGLE_RULES.items() if re.search(rule, norm(r["title"]))]
            angle_counts.update(matched_angles or ["otro"])
        pviews = [r["views"] for r in primary]
        recent_views = [r["views"] for r in recent_primary]
        share_rates = [r["shares"] / r["views"] * 100 for r in primary if r["views"]]
        er = [
            (r["likes"] + r["comments"] + r["shares"]) / r["views"] * 100
            for r in primary if r["views"]
        ]
        best = max(primary, key=lambda r: r["views"]) if primary else None
        recent_med = median(recent_views)
        historic_med = median([r["views"] for r in historical_primary])

        if len(primary) >= 10 or len(recent_primary) >= 4:
            if len(recent_primary) >= 3 and historic_med and recent_med < historic_med * 0.65:
                status = "SATURADO/EN DESCENSO"
            elif median(pviews) >= channel_median or (best and best["views"] >= top_cutoff):
                status = "PROFUNDO, AÚN PRODUCTIVO"
            else:
                status = "SATURADO/BAJO RETORNO"
        elif 2 <= len(primary) <= 6 and (
            median(pviews) >= channel_median * 1.25
            or (best and best["views"] >= top_cutoff)
            or median(share_rates) >= 0.40
        ):
            status = "SUBCUBIERTO CON SEÑAL"
        elif len(primary) <= 2 and best and best["views"] < channel_median * 0.5:
            status = "CASI NO PROBADO / SEÑAL DÉBIL"
        else:
            status = "COBERTURA MEDIA / INCONCLUSA"

        output.append({
            "entity": entity["name"],
            "type": entity["type"],
            "ecosystem": entity["ecosystem"],
            "primary_videos": len(primary),
            "mention_videos": len(mentions),
            "primary_60s_plus": sum(r["duration"] >= 60 for r in primary),
            f"primary_last_{args.recent_days}d": len(recent_primary),
            "median_views": round(median(pviews)),
            "recent_median_views": round(recent_med),
            "median_share_rate_pct": round(median(share_rates), 4),
            "median_engagement_rate_pct": round(median(er), 4),
            "top_10pct_hits": sum(r["views"] >= top_cutoff for r in primary),
            "best_views": best["views"] if best else 0,
            "best_date": best["date"] if best else "",
            "latest_date": max((r["date"] for r in primary), default=""),
            "dominant_angles": "; ".join(f"{k}:{v}" for k, v in angle_counts.most_common(3)),
            "status": status,
        })

    output.sort(key=lambda r: (-r["primary_videos"], -r["mention_videos"], r["entity"]))
    ecosystem_by_entity = {e["name"]: e["ecosystem"] for e in entities}
    ecosystem_rows = []
    for ecosystem in sorted(set(ecosystem_by_entity.values())):
        primary = [r for r in rows if ecosystem_by_entity.get(r["primary"]) == ecosystem]
        if not primary:
            continue
        recent = [r for r in primary if r["recent"]]
        views = [r["views"] for r in primary]
        recent_views = [r["views"] for r in recent]
        shares = [r["shares"] / r["views"] * 100 for r in primary if r["views"]]
        best = max(primary, key=lambda r: r["views"])
        angles = Counter()
        for r in primary:
            hits = [name for name, rule in ANGLE_RULES.items() if re.search(rule, norm(r["title"]))]
            angles.update(hits or ["otro"])
        ecosystem_rows.append({
            "ecosystem": ecosystem,
            "primary_videos": len(primary),
            "primary_60s_plus": sum(r["duration"] >= 60 for r in primary),
            f"primary_last_{args.recent_days}d": len(recent),
            "median_views": round(median(views)),
            "recent_median_views": round(median(recent_views)),
            "median_share_rate_pct": round(median(shares), 4),
            "top_10pct_hits": sum(v >= top_cutoff for v in views),
            "best_views": best["views"],
            "best_date": best["date"],
            "latest_date": max(r["date"] for r in primary),
            "dominant_angles": "; ".join(f"{k}:{v}" for k, v in angles.most_common(4)),
        })
    ecosystem_rows.sort(key=lambda r: (-r["primary_videos"], -r[f"primary_last_{args.recent_days}d"], r["ecosystem"]))
    args.csv.parent.mkdir(parents=True, exist_ok=True)
    with args.csv.open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output[0]))
        writer.writeheader()
        writer.writerows(output)
    args.json.write_text(json.dumps({
        "as_of": args.as_of,
        "catalog_videos": len(rows),
        "matched_primary_videos": sum(bool(r["primary"]) for r in rows),
        "unmatched_primary_videos": len(unmatched),
        "channel_median_views": round(channel_median),
        "top_10pct_view_cutoff": round(top_cutoff),
        "method": {
            "primary": "Entidad con mayor señal en título/caption previo a hashtags; desempate por primera aparición.",
            "mentions": "Cualquier alias reconocido en caption o hashtags.",
            "recent_days": args.recent_days,
        },
        "entities": output,
        "ecosystems": ecosystem_rows,
        "video_classification": rows,
        "unmatched": unmatched,
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"{len(output)} entidades; {len(rows)-len(unmatched)}/{len(rows)} videos con protagonista reconocido")


if __name__ == "__main__":
    main()
