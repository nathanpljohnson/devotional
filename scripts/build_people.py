# -*- coding: utf-8 -*-
"""Build data/people.json — who each voice was, and why they are in here."""
import json, pathlib, collections

ROOT = pathlib.Path(__file__).parent.parent
days = json.loads((ROOT / "data" / "days.json").read_text())["days"]

P = {
 "Augustine": ("354–430", "Bishop of Hippo in Roman North Africa",
   "Wrote The City of God after Rome was sacked in 410, to answer the charge that Christianity had made the "
   "empire weak. It is the founding text of Christian political thought and the reason 'two cities' language "
   "exists at all."),
 "John Chrysostom": ("c. 347–407", "Archbishop of Constantinople, called 'golden-mouthed'",
   "Preached against the wealth and flattery of the imperial court and was exiled twice for it, dying on a "
   "forced march. On the Priesthood is his argument for why he tried to avoid ordination."),
 "Gregory the Great": ("c. 540–604", "Pope, and a Roman prefect's son who ran the city's grain supply",
   "The Book of Pastoral Rule was written to explain why he did not want the papacy. It became the standard "
   "medieval manual on the duties of anyone holding office over others."),
 "Thomas Aquinas": ("1225–1274", "Dominican friar and theologian at Paris and Naples",
   "His treatment of law in the Summa is where the West gets the argument that an unjust law is not properly a "
   "law at all — the seed of every later appeal to a higher standard than statute."),
 "Thomas More": ("1478–1535", "Lord Chancellor of England under Henry VIII; executed for refusing the oath",
   "Utopia opens with a long argument about whether a person of conscience should serve a king he cannot fully "
   "obey. More eventually answered it with his life."),
 "Niccolò Machiavelli": ("1469–1527", "Florentine diplomat and civil servant",
   "The Prince is the most influential book ever written about political power detached from virtue. He is here "
   "as a genuine opponent, not a footnote — the case these passages have to answer."),
 "Hugo Grotius": ("1583–1645", "Dutch jurist; wrote much of his major work in prison and exile",
   "The Rights of War and Peace founded modern international law, including the idea that there are things you "
   "may not do to an enemy even when you are winning."),
 "John Milton": ("1608–1674", "Poet, and Secretary for Foreign Tongues to Cromwell's Council of State",
   "He defended regicide in print and went blind in government service. Paradise Lost gives the case for "
   "rebellion its most persuasive possible voice, which is part of its argument."),
 "Blaise Pascal": ("1623–1662", "Mathematician, inventor of the mechanical calculator, Jansenist",
   "The Pensées are notes for an unfinished defence of Christianity. His writing on kings, diversion, and human "
   "greatness-in-wretchedness is the sharpest short account of why power does not satisfy."),
 "Edmund Burke": ("1729–1797", "Irish-born MP in the British Parliament for nearly thirty years",
   "Prosecuted Warren Hastings over the conduct of the East India Company and defended the American colonists, "
   "then opposed the French Revolution. The founder of modern conservative political thought."),
 "Alexis de Tocqueville": ("1805–1859", "French aristocrat, magistrate, and later foreign minister",
   "Toured the United States in 1831 nominally to study prisons. Democracy in America is still the best outside "
   "account of how local self-government forms citizens."),
 "Ralph Waldo Emerson": ("1803–1882", "American essayist and former Unitarian minister",
   "Resigned his pulpit over conscience in 1832. Self-Reliance is the classic American argument for the "
   "individual against the pressure of the crowd."),
 "John Stuart Mill": ("1806–1873", "English philosopher, East India Company administrator, MP",
   "Educated brutally by his father to carry on Bentham's utilitarianism, which he then substantially revised. "
   "On Liberty is the strongest defence ever written of the dissenting minority of one."),
 "Søren Kierkegaard": ("1813–1855", "Danish philosopher who published much of his work pseudonymously",
   "Attacked the comfortable state Christianity of his own country. Fear and Trembling is about what it costs "
   "when a command comes to one person and cannot be justified to anyone else."),
 "Fyodor Dostoevsky": ("1821–1881", "Russian novelist; sentenced to death, reprieved at the scaffold, then four "
   "years in a Siberian prison camp",
   "No one has written better on what a man tells himself in order to do something monstrous, or on freedom as "
   "a burden people would rather hand to an authority."),
 "Leo Tolstoy": ("1828–1910", "Russian novelist and, later, radical Christian anarchist",
   "Fought at Sevastopol, then spent his last decades arguing that the Sermon on the Mount forbids force "
   "outright. His non-resistance writing directly shaped Gandhi and, through him, King."),
 "William Shakespeare": ("1564–1616", "English playwright",
   "The tragedies are the most exact study in the language of how a man reasons himself into a murder and then "
   "discovers that the killing has not finished."),
 "Marcus Aurelius": ("121–180", "Roman emperor for nineteen years, most of them at war",
   "The Meditations were private notes, never meant for publication — a working ruler talking himself into "
   "restraint, written in camp on the Danube frontier."),
 "G. K. Chesterton": ("1874–1936", "English journalist, critic, and Catholic apologist",
   "Argued in paradoxes because he thought the truth was shaped like one. Orthodoxy contains the best short "
   "account of why courage and humility are not opposites."),
 "C. S. Lewis": ("1898–1963", "Oxford and Cambridge medievalist; served in the trenches in 1917",
   "His essays on punishment and power are unusually alert to how much damage is done by people who are "
   "certain they are helping."),
 "Simone Weil": ("1909–1943", "French philosopher; factory worker by choice, then Republican volunteer in Spain",
   "Died at thirty-four in England, having restricted her food to the ration of occupied France. Wrote the "
   "essential modern essay on what force does to the person who uses it."),
 "Hannah Arendt": ("1906–1975", "German-Jewish political theorist; fled Germany in 1933 and France in 1941",
   "Reported on the Eichmann trial for The New Yorker and concluded that the worst crimes are often committed "
   "by unremarkable people who have stopped thinking."),
 "Aleksandr Solzhenitsyn": ("1918–2008", "Red Army artillery officer, then eight years in the Gulag",
   "The Gulag Archipelago got him deported from the USSR in 1974. He insisted the division between good and "
   "evil is not between camps or classes but inside each person."),
 "Shūsaku Endō": ("1923–1996", "Japanese Catholic novelist",
   "Silence follows a Portuguese missionary in seventeenth-century Japan pressed to renounce his faith to stop "
   "the torture of others. It is the great novel of moral failure and what God says in it."),
}

used = collections.defaultdict(list)
for k, d in days.items():
    for slot in ("voice1", "voice2"):
        if d.get(slot):
            used[d[slot]["author"]].append(int(k))

out = {}
for name, days_list in sorted(used.items()):
    if name not in P:
        raise SystemExit(f"missing bio for {name}")
    dates, role, why = P[name]
    out[name] = {"dates": dates, "role": role, "why": why, "days": sorted(set(days_list))}

missing = set(P) - set(used)
(ROOT / "data" / "people.json").write_text(json.dumps(out, ensure_ascii=False, indent=1))
print(f"{len(out)} people -> data/people.json")
if missing:
    print("bios written but unused:", missing)
for n, v in sorted(out.items(), key=lambda x: -len(x[1]["days"]))[:6]:
    print(f"  {n:24} days {v['days']}")
