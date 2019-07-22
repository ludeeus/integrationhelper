"""Web client."""
import asyncio
import socket
import aiohttp
import async_timeout


class WebClient:
    """Web client."""

    def __init__(self, session=None, logger=None):
        """
        Initialize.

        Usage:
        from integrationhelper.webclient import WebClient
        url = "https://sample.com/api"
        client = WebClient(aiohttp.ClientSession, mycustomlogger)
        client = WebClient(aiohttp.ClientSession)
        client = WebClient()
        myjson = await client.async_get_json(url, headers)
        myjson = await client.async_get_json(url)

        print(myjson)
        """
        self.session = session
        if logger is not None:
            self.logger = logger
        else:
            from integrationhelper.logger import Logger

            self.logger = Logger(__name__)

    async def async_get_json(self, url, custom_headers=None):
        """Get json response from server."""
        headers = {"Content-Type": "application/json"}
        if custom_headers is not None:
            for header in custom_headers:
                headers[header] = custom_headers[header]

        jsondata = None
        try:
            if self.session is not None:
                async with async_timeout.timeout(10, loop=asyncio.get_event_loop()):
                    response = await self.session.get(url, headers=headers)
                    jsondata = await response.json()
            else:
                async with aiohttp.ClientSession() as session:
                    async with async_timeout.timeout(10, loop=asyncio.get_event_loop()):
                        response = await session.get(url, headers=headers)
                        jsondata = await response.json()

            self.logger.debug(jsondata)

        except asyncio.TimeoutError as error:
            self.logger.error(
                f"Timeout error fetching information from {url} - ({error})"
            )
        except (KeyError, TypeError) as error:
            self.logger.error(f"Error parsing information from {url} - ({error})")
        except (aiohttp.ClientError, socket.gaierror) as error:
            self.logger.error(f"Error fetching information from {url} - ({error})")
        except Exception as error:  # pylint: disable=broad-except
            self.logger.error(f"Something really wrong happend! - ({error})")
        return jsondata
