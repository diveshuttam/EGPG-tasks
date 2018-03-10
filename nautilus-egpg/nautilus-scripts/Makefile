install: egpg_seal.sh egpg_open.sh egpg_sign.sh egpg_verify.sh
	chmod +x egpg_*.sh
	mkdir ~/.local/share/nautilus/scripts/egpg/ || echo directory exists
	cp egpg_*.sh ~/.local/share/nautilus/scripts/egpg/


uninstall: ~/.local/share/nautilus/scripts/egpg/
	rm -r ~/.local/share/nautilus/scripts/egpg/
