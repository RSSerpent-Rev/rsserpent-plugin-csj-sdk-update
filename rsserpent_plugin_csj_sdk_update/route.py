import json
import os
from typing import Any, cast

import arrow
from rsserpent_rev.utils import HTTPClient, cached

path = "/csj-sdk-update/{platform:int}"

source = "https://www.csjplatform.com/union/media/union/download/log?id=143&cate=1&backPath=/union/media/union/download/groMore"  # noqa: E501


@cached
async def provider(platform: int) -> dict[str, Any]:
    """Return the update logs of CSJ SDK."""
    async with HTTPClient() as client:
        cookies = {
            "sid_guard": cast(str, os.getenv("CSJ_SID_GUARD")),
        }

        response = await client.get(
            "https://www.csjplatform.com/union_pangle/api/access_document/list?",
            cookies=cookies,
        )

        logs = list(
            filter(lambda x: x["Id"] == platform, response.json()["data"]["list"])
        )[0]

        """Define a basic example data provider function."""
        return {
            "title": logs["Name"] + " 更新日志",
            "link": f"https://www.csjplatform.com/union/media/union/download/log?id={platform}",
            "description": logs["Name"],
            "items": [
                {
                    "title": f"{logs['Name']} {log['UpdateVersion']} 更新",
                    "description": log["UpdateInfo"],
                    "link": f"https://www.csjplatform.com/union/media/union/download/log?id={platform}",
                    "pub_date": arrow.get(log["UpdateDate"]),
                }
                for log in json.loads(logs["Log"])
            ],
        }
