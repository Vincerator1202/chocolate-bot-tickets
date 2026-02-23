package de.dev_MisterMo2022.farmwelt.Farmwelt.teleportsystems;

import org.bukkit.Location;
import org.bukkit.command.*;
import org.bukkit.entity.Player;

public class SpawnCommand implements CommandExecutor {

    @Override
    public boolean onCommand(CommandSender sender, Command cmd, String label, String[] args) {

        if (!(sender instanceof Player)) return true;
        Player player = (Player) sender;

        if (!FarmweltCore.instance.getConfig().contains("spawn")) {
            player.sendMessage("§cSpawn not set.");
            return true;
        }

        Location loc = (Location) FarmweltCore.instance.getConfig().get("spawn");
        player.teleport(loc);
        player.sendMessage("§aTeleported to spawn.");
        return true;
    }
}