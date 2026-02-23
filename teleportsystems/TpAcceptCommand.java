package de.dev_MisterMo2022.farmwelt.Farmwelt.teleportsystems;

import org.bukkit.command.*;
import org.bukkit.entity.Player;

import java.util.UUID;

public class TpAcceptCommand implements CommandExecutor {

    @Override
    public boolean onCommand(CommandSender sender, Command cmd, String label, String[] args) {

        if (!(sender instanceof Player)) return true;
        Player target = (Player) sender;

        UUID requesterUUID = FarmweltCore.instance.tpaRequests.get(target.getUniqueId());
        if (requesterUUID == null) {
            target.sendMessage("§cNo teleport requests.");
            return true;
        }

        Player requester = target.getServer().getPlayer(requesterUUID);
        if (requester != null) {
            requester.teleport(target.getLocation());
            requester.sendMessage("§aTeleport accepted!");
            target.sendMessage("§aPlayer teleported.");
        }

        FarmweltCore.instance.tpaRequests.remove(target.getUniqueId());
        return true;
    }
}