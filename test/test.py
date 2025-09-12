from pyvxlapi import (
    XLdriverConfig,
    xlGetDriverConfig,
)

driver_config = XLdriverConfig()
status = xlGetDriverConfig(driver_config)
print(status)

for i in range(driver_config.channelCount):
    channel_config = driver_config.channel[i]
    print(f"{i} {channel_config.name} {channel_config.channelMask}")
