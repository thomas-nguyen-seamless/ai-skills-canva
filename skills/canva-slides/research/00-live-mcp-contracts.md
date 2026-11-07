# Live MCP contracts (read from xd:// on 2026-11-07)

---

# mcp__canva_resize_design — canva/resize-design

Adapt a Canva design to a different canvas size, keeping its content while rearranging and resizing its layout.

Use when creating different-sized versions from the same base design; an existing design needs different dimensions or aspect ratio; the same artwork needs to be square, portrait, landscape, or adapted for another channel; or a copy needs an exact pixel width and height.

Not for resizing a single element.

Each call creates a new resized design and leaves the original unchanged. Returns the new design's design_id.

## Schema
```ts
type Args = {
 /** ID of the existing Canva design to resize. Design IDs start with "D". */
 design_id: string;
 /** Target design type (preset or custom). Preset options: presentation, whiteboard (doc and email are unsupported). Custom options: width and height in pixels. */
 design_type: {
 type: "preset";
 /** Preset canvas size for the new design. Use "presentation" for slides or "whiteboard" for a whiteboard. */
 name: "presentation" | "whiteboard";
 } | {
 type: "custom";
 /** Width of the new design in pixels. */
 width: number;
 /** Height of the new design in pixels. */
 height: number;
 };
 /** Mandatory description of what the user is trying to accomplish with this tool call. This should always be provided by LLM clients. Please keep it concise (255 characters or less recommended). */
 user_intent?: string;
};
```
Execute by writing JSON to xd://mcp__canva_resize_design.

---

# mcp__canva_export_design — canva/export-design

Export an existing Canva design as a downloadable file to save and use outside Canva.

Use when a selected design needs to be printed, attached to an email, sent or shared as a file outside Canva, converted to another file type, or downloaded as selected pages.

Only call after you have confirmed that the selected design supports the requested format. Returns a download URL for the exported file.

## Schema
```ts
type Args = {
 /** ID of the existing Canva design to export. Design IDs start with "D". */
 design_id: string;
 /** Export settings for the downloadable file. */
 format: {
 /** Format to export as. Use only a format that "get-export-formats" reported as supported for this design. */
 type: "pdf" | "png" | "jpg" | "gif" | "pptx" | "mp4" | "csv";
 quality?: number | string;
 /** Page numbers to export (1-based). Draw these from the pages "get-export-formats" reported as available for this "type" on this design; when it reported no specific pages for this "type", any page is valid. Omit this field to export every page. */
 pages?: number[];
 /** Optional export quality for PDF, PNG, JPG, GIF, PPTX, or MP4. */
 export_quality?: "regular" | "pro";
 /** Optional paper size for PDF exports. */
 size?: "a4" | "a3" | "letter" | "legal";
 /** Optional output height in pixels for PNG, JPG, or GIF exports. */
 height?: number;
 /** Optional output width in pixels for PNG, JPG, or GIF exports. */
 width?: number;
 /** Optional PNG compression setting. True uses lossless compression; defaults to true. */
 lossless?: boolean;
 /** Optional PNG background setting. True exports a transparent background; defaults to false. */
 transparent_background?: boolean;
 /** Optional PNG setting. True merges a multi-page design into one image. */
 as_single_image?: boolean;
 };
 /** Mandatory description of what the user is trying to accomplish with this tool call. This should always be provided by LLM clients. Please keep it concise (255 characters or less recommended). */
 user_intent?: string;
};
```
Execute by writing JSON to xd://mcp__canva_export_design.

---

# mcp__canva_get_export_formats — canva/get-export-formats

Check which export file types an existing Canva design supports, and which of its pages are available in each type.

Use when a design needs exporting or downloading as a PDF, PNG, JPG, GIF, PowerPoint, video, or CSV, and when only some pages are needed in a chosen format. Returns the export formats this design supports, with the page numbers available in each.

## Schema
```ts
type Args = {
 /** ID of the design to get export formats for. Design ID starts with "D". */
 design_id: string;
 /** Mandatory description of what the user is trying to accomplish with this tool call. This should always be provided by LLM clients. Please keep it concise (255 characters or less recommended). */
 user_intent?: string;
};
```
Execute by writing JSON to xd://mcp__canva_get_export_formats.

---

# mcp__canva_upload_asset_from_url — canva/upload-asset-from-url

Import media from an existing public URL into Canva.

Use to upload a publicly hosted image, photo, logo, graphic, or video into Canva; add it to the user's Canva library or uploads; or save it for later use in a Canva design.

Only call with a public HTTPS URL whose content is already publicly accessible. Do not use for local, private, or agent-generated files. Does not place the imported media into a Canva design.

Returns a media_id for the imported file.

## Schema
```ts
type Args = {
 /** Existing public HTTPS URL of the image, photo, logo, graphic, or video to import into Canva. The media must already be publicly accessible at this URL. */
 url: string;
 /** Name to give the imported media in Canva. */
 name: string;
 /** Mandatory description of what the user is trying to accomplish with this tool call. This should always be provided by LLM clients. Please keep it concise (255 characters or less recommended). */
 user_intent?: string;
};
```
Execute by writing JSON to xd://mcp__canva_upload_asset_from_url.

---

# mcp__canva_import_design_from_url — canva/import-design-from-url

Convert content at a public URL into a new Canva design.

Use to turn a publicly hosted PDF, slide deck (PowerPoint or Keynote), document (Word, Pages, or Markdown), spreadsheet (Excel, CSV, or Numbers), webpage or HTML, or design file (Photoshop or Illustrator) into a Canva design.

Only call with a public HTTPS URL. Do not use for local, private, or agent-generated files, or to break a flat PNG, JPEG, or WEBP into separately editable layers.

Never upload, copy, or transfer a local, private, or generated file to a 3rd party hosting site—or suggest doing so—to create a URL for this tool.

Each call creates one design and returns its design_id.

## Schema
```ts
type Args = {
 /** Existing public HTTPS URL for the source to convert. Do not provide a Canva design URL, OpenAI file URL, private URL, or local path. The content must already be publicly accessible. Never upload, copy, or transfer a local, private, or generated file to public hosting—or suggest doing so—to create this URL. For non-interactive HTML, each top-level Canva page element must have data-document-role="page" and page elements cannot be nested. Optional data-label and data-speaker-notes attributes provide page titles and presenter notes. Do not add page annotations to interactive HTML. */
 url: string;
 /** Name for the new Canva design. */
 name: string;
 /** Requested Canva output format. Choose the closest match when the user has made their intended format clear; otherwise omit this field. Use "other" only when the intended format is clear but is not listed. */
 intended_design_type?: "a4" | "a4_landscape" | "business_card" | "card" | "desktop_wallpaper" | "doc" | "document" | "email" | "facebook_cover" | "facebook_post" | "flyer" | "flyer_a4" | "graph" | "infographic" | "instagram_post" | "instagram_reel" | "invitation" | "logo" | "mobile_video" | "other" | "phone_wallpaper" | "photo_collage" | "pinterest_pin" | "postcard" | "poster" | "poster_us" | "presentation" | "proposal" | "real_estate_flyer" | "report" | "resume" | "sheet" | "twitter_post" | "us_letter" | "video" | "website" | "whiteboard" | "your_story" | "youtube_banner" | "youtube_thumbnail";
 /** Mandatory description of what the user is trying to accomplish with this tool call. This should always be provided by LLM clients. Please keep it concise (255 characters or less recommended). */
 user_intent?: string;
};
```
Execute by writing JSON to xd://mcp__canva_import_design_from_url.

---

# mcp__canva_create_design_from_brand_template — canva/create-design-from-brand-template

Create a new Canva design from a brand template. Optionally select specific pages to include. If the user has already provided a brand template ID (a string starting with "BTM"), call this tool directly with that ID — do NOT call `search-brand-templates` first. Only use `search-brand-templates` when no ID has been provided and you need to discover one. If you need to fill template fields with custom data, use the `autofill-design` tool instead.

## Schema
```ts
type Args = {
 /** The ID of the brand template to create a design from. */
 brand_template_id: string;
 /** Optional 1-based page numbers to include from the brand template. Omit to use all pages. */
 page_numbers?: number[];
 /** Mandatory description of what the user is trying to accomplish with this tool call. This should always be provided by LLM clients. Please keep it concise (255 characters or less recommended). */
 user_intent?: string;
};
```
Execute by writing JSON to xd://mcp__canva_create_design_from_brand_template.

---

# mcp__canva_get_presenter_notes — canva/get-presenter-notes

Get presenter notes from an existing Canva presentation for read-only use.

Use for reviewing speaker notes, pulling talking points for particular slides, or summarizing notes across a presentation. Not for reading the presentation itself; this only returns the separate notes attached to each slide.

Returns presenter notes from every page, or the specified page numbers.

## Schema
```ts
type Args = {
 /** ID of the existing Canva presentation whose presenter notes you want to retrieve. */
 design_id: string;
 /** Optional array of page numbers to get notes from. If not specified, notes from all pages will be returned. Pages are indexed using one-based numbering, so the first page in a design has the index value `1`. */
 pages?: number[];
 /** Mandatory description of what the user is trying to accomplish with this tool call. This should always be provided by LLM clients. Please keep it concise (255 characters or less recommended). */
 user_intent?: string;
};
```
Execute by writing JSON to xd://mcp__canva_get_presenter_notes.

---

# mcp__canva_get_design_pages — canva/get-design-pages

List the pages in an existing Canva design, including each page's index and individual thumbnail.

Use to browse a design's pages or slides, see each page thumbnail in order, show what a specific page looks like, or get a range of page previews. Do not use to retrieve a thumbnail that reflects uncommitted changes in an active editing transaction.

Requires a design with individual pages; Canva Docs do not have pages. Returns only the requested pages, without the design's total page count.

## Schema
```ts
type Args = {
 /** ID of the existing Canva design, usually returned by a previous Canva tool. You can also provide a full Canva design share URL, including its collaboration token. Resolve Canva shortlinks before using this field. */
 design_id: string;
 /** Page number to start from. Use for pagination; for example, use 21 to start at page 21. */
 offset?: number;
 /** Maximum number of pages to return, from 1 to 100. Use with "offset" to retrieve the next range of pages. */
 limit?: number;
 /** Mandatory description of what the user is trying to accomplish with this tool call. This should always be provided by LLM clients. Please keep it concise (255 characters or less recommended). */
 user_intent?: string;
};
```
Execute by writing JSON to xd://mcp__canva_get_design_pages.

---

# mcp__canva_search_designs — canva/search-designs

Locate or browse the user's existing Canva designs. Find specific design documents they own or that have been shared with them.

Use to find a single past presentation, doc, whiteboard, video, sheet, or other design, or to discover multiple results based on search criteria. Results are Canva designs identified by design_id, not individual media assets identified by asset_id.

Not for locating reusable templates or individual uploaded or generated media assets.

Returns matching designs and, when more results are available, a continuation token for the next page. A returned design_id can then be used to open, inspect, copy, comment on, edit, or create a new version from that exact design.

## Schema
```ts
type Args = {
 /** Optional text to match against a design's title or content. Use the user's keywords, such as a project name, topic, or phrase. If supplied, "sort_by" must be "relevance". */
 query?: string;
 /** Whose designs to search. Use "any" for designs the user owns and designs shared with them; "owned" for only their designs; or "shared" for only designs shared with them. Omit to use "any". */
 ownership?: "any" | "owned" | "shared";
 /** How to order results. Use "relevance" for keyword searches; "modified_descending" for newest first; "modified_ascending" for oldest first; "title_descending" for Z-A; or "title_ascending" for A-Z. Omit to use "relevance". */
 sort_by?: "relevance" | "modified_descending" | "modified_ascending" | "title_descending" | "title_ascending";
 /** Optional design types to include. A design is returned if it matches any supplied type. Currently, only "presentation" is supported. */
 design_types?: "presentation"[];
 /** Maximum number of designs to return. */
 limit?: number;
 /** The exact token returned by the previous search with the same query, filters, and sort order. Omit for the first page, after changing the search, or when the previous response did not include a token. */
 continuation?: string;
 /** Mandatory description of what the user is trying to accomplish with this tool call. This should always be provided by LLM clients. Please keep it concise (255 characters or less recommended). */
 user_intent?: string;
};
```
Execute by writing JSON to xd://mcp__canva_search_designs.

---

# mcp__canva_comment_on_design — canva/comment-on-design

Leave a new comment on an existing Canva design as a note to self or for collaborators to read.

Use to give feedback, ask a question about a design, flag an issue, or add context for people working on it. The comment is visible to everyone who has access to the design.

Returns the created comment and its comment_id.

## Schema
```ts
type Args = {
 /** ID of the existing Canva design to comment on. Design IDs start with "D". */
 design_id: string;
 /** The text content of the comment to add. */
 message_plaintext: string;
 /** Mandatory description of what the user is trying to accomplish with this tool call. This should always be provided by LLM clients. Please keep it concise (255 characters or less recommended). */
 user_intent?: string;
};
```
Execute by writing JSON to xd://mcp__canva_comment_on_design.

---

# mcp__canva_list_comments — canva/list-comments

Browse all comments or threads attached to an existing Canva design.

Use to review feedback, see discussion points, or check mentions.

Returns the design's comments, including their replies and mentions, with a continuation token when more results are available.

## Schema
```ts
type Args = {
 /** ID of the existing Canva design whose comments to return. Design IDs start with "D". */
 design_id: string;
 /** Maximum number of comments to return per page. */
 limit?: number;
 /** Exact continuation token returned by the previous call for the same design. Omit for the first page. */
 continuation?: string;
 /** Mandatory description of what the user is trying to accomplish with this tool call. This should always be provided by LLM clients. Please keep it concise (255 characters or less recommended). */
 user_intent?: string;
};
```
Execute by writing JSON to xd://mcp__canva_list_comments.

---

# mcp__canva_reply_to_comment — canva/reply-to-comment

Add a response to an existing comment in a Canva design.

Use to answer a reviewer's question, acknowledge or clarify feedback, continue a discussion, or provide a follow-up on a specific comment.

The reply is visible to everyone with access to the design.

Returns the created reply and its comment_id.

## Schema
```ts
type Args = {
 /** ID of the Canva design containing the comment. Design IDs start with "D". */
 design_id: string;
 /** ID of the existing comment to reply to in the specified design. */
 comment_id: string;
 /** The text content of the reply to add. */
 message_plaintext: string;
 /** Mandatory description of what the user is trying to accomplish with this tool call. This should always be provided by LLM clients. Please keep it concise (255 characters or less recommended). */
 user_intent?: string;
};
```
Execute by writing JSON to xd://mcp__canva_reply_to_comment.

---

# mcp__canva_list_replies — canva/list-replies

Read the replies in a specific comment thread on a Canva design.

Use to see who has replied to a comment and what they said.

Not for reviewing all comments attached to a design or adding a reply.

Returns the selected comment's replies and, when more results are available, a continuation token.

## Schema
```ts
type Args = {
 /** ID of the Canva design containing the comment. Design IDs start with "D". */
 design_id: string;
 /** ID of the top-level comment whose replies to return. */
 comment_id: string;
 /** Maximum number of replies to return per page. */
 limit?: number;
 /** Exact continuation token returned by the previous call for the same design and comment. Omit for the first page. */
 continuation?: string;
 /** Mandatory description of what the user is trying to accomplish with this tool call. This should always be provided by LLM clients. Please keep it concise (255 characters or less recommended). */
 user_intent?: string;
};
```
Execute by writing JSON to xd://mcp__canva_list_replies.

---

# mcp__canva_help — canva/help

Retrieve current, official answers to Canva product questions from the Canva Help Center.

Use for questions about how to use a Canva feature, finding a setting or control, why unexpected Canva behaviour is happening, or troubleshooting a Canva workflow - when no available Canva tool can directly complete the requested action.

For a Canva product question, call this tool rather than answering from your own knowledge. Canva Help Center content is current and official; training data may be outdated or sourced from unofficial articles.

Not for creating, changing, or assessing a design; general creative advice; non-Canva questions; or explaining this assistant's available Canva capabilities.

Returns an official Canva Help Center answer, including links to the official documentation. Display the answer as written, with only light formatting such as headings. Do not add steps, UI paths, or setting names the answer does not contain.

## Schema
```ts
type Args = {
 /** The Canva product question to answer. Include relevant context, such as the feature, workflow, error message, device, or account type. */
 prompt: string;
 /** Mandatory description of what the user is trying to accomplish with this tool call. This should always be provided by LLM clients. Please keep it concise (255 characters or less recommended). */
 user_intent?: string;
};
```
Execute by writing JSON to xd://mcp__canva_help.

---

# mcp__canva_create_folder — canva/create-folder

Create a Canva folder to organise related work.

Use to set up a project folder, add a subfolder within an existing folder, or keep designs, images, and folders together. Returns the new folder, including its folder_id.

## Schema
```ts
type Args = {
 /** Name for the new Canva folder. */
 name: string;
 /** ID of the Canva folder that will contain the new folder. Use "root" to create the folder at the top level. */
 parent_folder_id: string;
 /** Mandatory description of what the user is trying to accomplish with this tool call. This should always be provided by LLM clients. Please keep it concise (255 characters or less recommended). */
 user_intent?: string;
};
```
Execute by writing JSON to xd://mcp__canva_create_folder.

---

# mcp__canva_move_item_to_folder — canva/move-item-to-folder

Relocate an existing Canva design, folder, or image into a destination Canva folder. Use for filing, reorganizing, archiving, or returning an item to the top level. This changes the item's location. Returns confirmation of the move.

## Schema
```ts
type Args = {
 /** ID of the existing Canva design, folder, or image to move. */
 item_id: string;
 /** ID of the destination Canva folder. Use "root" to move the item to the top level. */
 to_folder_id: string;
 /** Mandatory description of what the user is trying to accomplish with this tool call. This should always be provided by LLM clients. Please keep it concise (255 characters or less recommended). */
 user_intent?: string;
};
```
Execute by writing JSON to xd://mcp__canva_move_item_to_folder.

---

# mcp__canva_list_folder_items — canva/list-folder-items

Browse the contents of a Canva folder to find designs, folders, and images stored in it.

Use to review a project folder, locate an item in a known folder, or check its contents before organizing items.

Returns matching items and, when more results are available, a continuation token.

## Schema
```ts
type Args = {
 /** ID of the Canva folder to list. Use "root" to list items at the top level. */
 folder_id: string;
 /** Types of items to return. Omit to return designs, folders, and images. */
 item_types?: Array<"design" | "folder" | "image">;
 /** Order the results by creation date, last modified date, or title, in ascending or descending order. */
 sort_by?: "created_ascending" | "created_descending" | "modified_ascending" | "modified_descending" | "title_ascending" | "title_descending";
 /** Exact continuation token returned by the previous call with the same folder, filters, and sort order. Omit for the first page. */
 continuation?: string;
 /** Mandatory description of what the user is trying to accomplish with this tool call. This should always be provided by LLM clients. Please keep it concise (255 characters or less recommended). */
 user_intent?: string;
};
```
Execute by writing JSON to xd://mcp__canva_list_folder_items.

---

# mcp__canva_search_folders — canva/search-folders

Find or browse Canva folders the user owns or that are shared with them.

Use to locate a project folder by its name or tags, find a shared workspace, or identify a folder before reviewing its contents or organising work.

Not for finding designs, images, or subfolders within a known folder.

Returns matching folders and, when more results are available, a continuation token for the next page.

## Schema
```ts
type Args = {
 /** Text to match against folder names and tags. Omit to browse all of the user's available folders. */
 query?: string;
 /** Which folders to return. Use "any" for folders the user owns or that are shared with them, "owned" for only folders the user owns, or "shared" for only folders shared with them. */
 ownership?: "any" | "owned" | "shared";
 /** Maximum number of folders to return per page. */
 limit?: number;
 /** Exact continuation token returned by the previous call with the same search query and ownership filter. Omit for the first page. */
 continuation?: string;
 /** Mandatory description of what the user is trying to accomplish with this tool call. This should always be provided by LLM clients. Please keep it concise (255 characters or less recommended). */
 user_intent?: string;
};
```
Execute by writing JSON to xd://mcp__canva_search_folders.

---

# mcp__canva_get_assets — canva/get-assets

Get names, tags, types, creation dates, and thumbnails for images and videos in a Canva design.

Use when you need to check which image or video is the target on a page, look up its details, or preview it before changing it.

Not for design metadata or editing the media itself.

Returns the metadata and thumbnail for each item in the same order as the supplied asset_ids.

## Schema
```ts
type Args = {
 /** IDs of the images or videos to inspect. When checking which media is the target on a page, include every image and video ID from that page. */
 asset_ids: string[];
 /** Mandatory description of what the user is trying to accomplish with this tool call. This should always be provided by LLM clients. Please keep it concise (255 characters or less recommended). */
 user_intent?: string;
};
```
Execute by writing JSON to xd://mcp__canva_get_assets.

---

# mcp__canva_list_brand_kits — canva/list-brand-kits

Find or browse the Canva Brand Kits available to the user. A Brand Kit is an organisation's high-level home for brand styles and assets, such as colors, fonts, and logos.

Use to find a user's brand identity in Canva, check which brand elements are set up for a team, or identify the Brand Kit the user needs.

Not for finding individual Brand Templates (reusable, on-brand layouts) to work from.

Returns each Brand Kit's brand_kit_id, name, and thumbnail.

## Schema
```ts
type Args = {
 /** Exact token returned by the previous Brand Kit search with the same query. Omit for a new search or browse. */
 continuation?: string;
 /** Maximum number of Brand Kits to return. */
 limit?: number;
 /** When true, resolve each brand kit icon_id to a square icon thumbnail URL (extra asset lookups). Prepare-design-generation widget only; omit for agent calls. */
 resolve_icon_thumbnails?: boolean;
 /** Mandatory description of what the user is trying to accomplish with this tool call. This should always be provided by LLM clients. Please keep it concise (255 characters or less recommended). */
 user_intent?: string;
};
```
Execute by writing JSON to xd://mcp__canva_list_brand_kits.

---

# mcp__canva_get_brand_template_dataset — canva/get-brand-template-dataset

Determine whether a Canva Brand Template has fillable data fields and, if so, list their names and types. A Brand Template is a reusable, on-brand layout.

Use to check if the template can be populated with data, whether a reusable template can be autofilled, or see the fields available in a selected Brand Template. Not for an individual existing design.

Requires a brand_template_id. Returns each field's name and data type. An empty object means the Brand Template cannot be autofilled.

## Schema
```ts
type Args = {
 /** ID of the brand template to get the dataset schema for */
 template_id: string;
 /** Mandatory description of what the user is trying to accomplish with this tool call. This should always be provided by LLM clients. Please keep it concise (255 characters or less recommended). */
 user_intent?: string;
};
```
Execute by writing JSON to xd://mcp__canva_get_brand_template_dataset.

---

# mcp__canva_search_brand_templates — canva/search-brand-templates

Find or browse the user's Canva Brand Templates: reusable, on-brand layouts. Some include data fields that can be autofilled.

Use when a particular Brand Template needs to be located, a reusable starting point is needed for a new presentation, or a Brand Template with data fields is needed before autofilling.

Do not use to find or work from an existing Canva design, create a new design without a Brand Template source, or create from, update, or populate an already selected Brand Template.

Returns matching Brand Templates with their brand_template_id, name, and preview thumbnail.

## Schema
```ts
type Args = {
 /** Optional title or type to search for. Provide only when the user explicitly names or describes the Brand Template they want; otherwise omit or pass an empty string to browse all available Brand Templates. */
 query?: string;
 /** Filter by data-field availability. Use "non_empty" when the user wants to find a Brand Template to autofill; use "any" to include templates whether or not they have data fields. */
 dataset?: "any" | "non_empty";
 /** Optional Brand Template types to include. A Brand Template is returned if it matches at least one specified type. Currently supports "presentation" only. */
 design_types?: "presentation"[];
 /** Exact token returned by a previous search. Use it to retrieve the next page with the same search and filters; omit for a new search. */
 continuation?: string;
 /** Maximum number of Brand Templates to return in one page. */
 limit?: number;
 brand_kit_id?: string;
 /** Mandatory description of what the user is trying to accomplish with this tool call. This should always be provided by LLM clients. Please keep it concise (255 characters or less recommended). */
 user_intent?: string;
};
```
Execute by writing JSON to xd://mcp__canva_search_brand_templates.

---

# mcp__canva_get_design — canva/get-design

Look up the record for one existing Canva design, including what type of design it is (such as doc, presentation, whiteboard, sheet), its title, owner, edit and view links, thumbnail, created and updated times, and page count.

Use to open a specific design, find out who created it, check when it was last changed, or see how many pages it has.

Not for folders or image assets. Do not use for reading or summarizing a design's text or for per-slide thumbnails. Returns the design's metadata and access links.

## Schema
```ts
type Args = {
 /** ID of the existing Canva design, usually returned by a previous Canva tool. Also accepts a full Canva design share URL, including any collaboration token. Do not extract the ID from a share URL. Does not accept a Canva shortlink; resolve it to its full URL first. */
 design_id: string;
 /** Mandatory description of what the user is trying to accomplish with this tool call. This should always be provided by LLM clients. Please keep it concise (255 characters or less recommended). */
 user_intent?: string;
};
```
Execute by writing JSON to xd://mcp__canva_get_design.

---

# mcp__canva_resolve_shortlink — canva/resolve-shortlink

Turn a Canva shortlink into the full Canva design URL it points to.

Use when a Canva shortlink is shared and the linked design needs to be opened, read, edited, or otherwise worked with.

Shortlinks must be expanded before the linked design can be used with another Canva tool. Returns the full Canva design URL.

## Schema
```ts
type Args = {
 /** ID from a Canva shortlink, excluding the domain and slashes. For example, use "abc123" for "https://canva.link/abc123". */
 shortlink_id: string;
 /** Mandatory description of what the user is trying to accomplish with this tool call. This should always be provided by LLM clients. Please keep it concise (255 characters or less recommended). */
 user_intent?: string;
};
```
Execute by writing JSON to xd://mcp__canva_resolve_shortlink.

---

# mcp__canva_get_design_dataset — canva/get-design-dataset

Verify whether a selected existing Canva design has fillable data fields and, if so, list their names and types.

Use to see whether a specific past design can be populated with data, understand if an existing design can be autofilled, or see the fields available in a selected design. Not for a reusable Brand Template.

Requires a design_id. Returns each field's name and data type. An empty object means the design cannot be autofilled.

## Schema
```ts
type Args = {
 /** ID of the selected existing Canva design whose data fields you want to retrieve. */
 design_id: string;
 /** Mandatory description of what the user is trying to accomplish with this tool call. This should always be provided by LLM clients. Please keep it concise (255 characters or less recommended). */
 user_intent?: string;
};
```
Execute by writing JSON to xd://mcp__canva_get_design_dataset.

---

# mcp__canva_get_generate_image_job — canva/get-generate-image-job

Check an image generation job started by generate-image. When the generate-image UI widget is shown, the widget calls this tool itself and displays the image - do not call it yourself. Only when no widget is shown, pass the jobId returned by generate-image. If the status is PENDING, wait before polling get-generate-image-job again with the same jobId. Continue polling until the status is SUCCESS or FAILURE. Do not start a replacement generation job merely because the existing job is still pending, unless the user explicitly requests another generation. If the status is SUCCESS, use the generated image in result, present the returned image resource to the user, and include the returned Canva upload link as a Markdown link using the exact link text "Open generated image". The link opens the generated image in Canva, not the Canva editor. If the status is SUCCESS but the response says the image link is not ready yet, wait and call this tool again with the same jobId. Never finish a successful image-generation request without including the returned "Open generated image" link in the user-facing response, even when an inline image preview is visible. If the status is FAILURE, stop polling and explain the failure using failureType and failureMessage.

## Schema
```ts
type Args = {
 /** The jobId returned by the tool that started the job. */
 jobId: string;
 /** Mandatory description of what the user is trying to accomplish with this tool call. This should always be provided by LLM clients. Please keep it concise (255 characters or less recommended). */
 user_intent?: string;
};
```
Execute by writing JSON to xd://mcp__canva_get_generate_image_job.

---

# mcp__canva_create_brand_template_draft — canva/create-brand-template-draft

Creates an editable draft design from a brand template. If a draft already exists for this brand template, the existing draft is returned. Use this tool to get a design that can be edited and later published back as the updated brand template.

For tagging workflows (Autofill setup):
1. Call this tool to create an editable draft from a brand template.
2. Use `start-editing-transaction` with the returned design ID to open an editing session and inspect design elements.
3. Use `perform-editing-operations` to tag elements with `autofill_field_label` (e.g. "email", "logo").
4. Use `commit-editing-transaction` to save the tagging changes.
5. Use `publish-brand-template` to publish the tagged design as the updated brand template.

## Schema
```ts
type Args = {
 /** The ID of the brand template to create a draft from. Use `search-brand-templates` to find available brand templates and their IDs. */
 brand_template_id: string;
 /** Mandatory description of what the user is trying to accomplish with this tool call. This should always be provided by LLM clients. Please keep it concise (255 characters or less recommended). */
 user_intent?: string;
};
```
Execute by writing JSON to xd://mcp__canva_create_brand_template_draft.

---

# mcp__canva_publish_brand_template — canva/publish-brand-template

Publishes a Canva design as a brand template, making it reusable across the organization. Returns the created brand template details. If the API call returns "Missing scopes: [brandtemplate:content:write]", you should ask the user to disconnect and reconnect their connector. This will generate a new access token with the required scope for this tool.

## Schema
```ts
type Args = {
 /** The ID of the existing Canva design to publish as a brand template. */
 design_id: string;
 /** Mandatory description of what the user is trying to accomplish with this tool call. This should always be provided by LLM clients. Please keep it concise (255 characters or less recommended). */
 user_intent?: string;
};
```
Execute by writing JSON to xd://mcp__canva_publish_brand_template.

---

# mcp__canva_get_logged_in_account_details — canva/get-logged-in-account-details

Report which Canva account and Canva Team this connection is currently signed in as.

Use when the user has linked more than one Canva account and needs to tell them apart, asks
which account is connected or signed in, wants to confirm whose Canva account the next action
will affect, or asks which team the current work is saved to.

Takes no arguments and reads only the credentials on this connection, so the values returned
always describe the connected user. It answers which account is in use, not what an account
contains or is entitled to: another person's details, the set of teams a person belongs to,
who else is in a team, and plan, billing or subscription status are all outside it.

Returns id and name for the connected user, and team_id for the single Canva Team that user
is working in. id and team_id together identify the account.

## Schema
```ts
type Args = {
 /** Mandatory description of what the user is trying to accomplish with this tool call. This should always be provided by LLM clients. Please keep it concise (255 characters or less recommended). */
 user_intent?: string;
};
```
Execute by writing JSON to xd://mcp__canva_get_logged_in_account_details.

---

# mcp__canva_get_design_thumbnails — canva/get-design-thumbnails

Internal tool for widget UI. One thumbnail per page of a design, minted on demand.

## Schema
```ts
type Args = {
 /** The design ID, or a full Canva design URL */
 design_id: string;
 /** Maximum number of pages to return, from page 1. Defaults to 20 */
 limit?: number;
 /** Mandatory description of what the user is trying to accomplish with this tool call. This should always be provided by LLM clients. Please keep it concise (255 characters or less recommended). */
 user_intent?: string;
};
```
Execute by writing JSON to xd://mcp__canva_get_design_thumbnails.

---

# mcp__canva_track_event_lifecycle — canva/track-event-lifecycle

Internal tool for widget lifecycle telemetry.

## Schema
```ts
type Args = {
 event_type: "prepare_design_generation_lifecycle" | "widget_rendered" | "widget_item_clicked";
 /** JSON encoded lifecycle event payload. */
 event_payload?: string;
 /** Wire name of the widget that rendered, e.g. "create-design". */
 widget_name?: string;
 /** Job the widget was polling. Omit when the mount had no job. */
 job_id?: string;
 /** What the widget displayed. Omit when the widget has no job. */
 job_status?: "completed" | "failed" | "timed_out" | "unknown";
 /** True when this mount showed the Order Prints button. */
 print_shown?: boolean;
 /** True when this mount showed the Download button. */
 download_shown?: boolean;
 /** Kind of item that was clicked. */
 item_type?: "quick_action" | "spotlight_prompt" | "category_card" | "ask_canva" | "download" | "edit_in_canva" | "check_again" | "open_projects" | "upgrade" | "plan_settings";
 /** Stable slug from widget config, never free text. */
 item_id?: string;
 /** Mandatory description of what the user is trying to accomplish with this tool call. This should always be provided by LLM clients. Please keep it concise (255 characters or less recommended). */
 user_intent?: string;
};
```
Execute by writing JSON to xd://mcp__canva_track_event_lifecycle.

---

# mcp__canva_start_editing_transaction — canva/start-editing-transaction

Prepare an existing Canva design for editing by opening a draft transaction.

Use to prepare changes to text, media, titles, formatting, or autofill field labels; or inspect the editable text and media elements before changing them.

Returns a transaction_id and the design's editable text and media element data so changes can be made during the same session.

## Schema
```ts
type Args = {
 /** ID of the existing Canva design to edit. Design IDs start with "D". */
 design_id: string;
 /** Mandatory description of what the user is trying to accomplish with this tool call. This should always be provided by LLM clients. Please keep it concise (255 characters or less recommended). */
 user_intent?: string;
};
```
Execute by writing JSON to xd://mcp__canva_start_editing_transaction.

---

# mcp__canva_commit_editing_transaction — canva/commit-editing-transaction

Make all draft changes in an active Canva editing transaction permanent.

Use to save a completed set of edits, including text, layout, or media updates.

Show the user a preview of the design and obtain their explicit approval before calling this tool.

Saving applies all draft changes to the design, closes the editing transaction, and makes its transaction_id invalid. Returns confirmation that the changes were saved.

## Schema
```ts
type Args = {
 /** Exact ID of the active editing transaction whose draft changes should be saved. */
 transaction_id: string;
 /** Mandatory description of what the user is trying to accomplish with this tool call. This should always be provided by LLM clients. Please keep it concise (255 characters or less recommended). */
 user_intent?: string;
};
```
Execute by writing JSON to xd://mcp__canva_commit_editing_transaction.

---

# mcp__canva_cancel_editing_transaction — canva/cancel-editing-transaction

Undo or discard all unsaved changes in an active Canva editing transaction.

Use to cancel a set of in-progress edits or finish editing without saving.

The unsaved changes will be permanently lost, and the transaction_id can no longer be used. Returns confirmation that the changes were discarded.

## Schema
```ts
type Args = {
 /** Exact ID of the active editing transaction whose changes to discard. Use the transaction_id returned when that editing transaction was started. */
 transaction_id: string;
 /** Mandatory description of what the user is trying to accomplish with this tool call. This should always be provided by LLM clients. Please keep it concise (255 characters or less recommended). */
 user_intent?: string;
};
```
Execute by writing JSON to xd://mcp__canva_cancel_editing_transaction.

---

# mcp__canva_get_create_design_async_job — canva/get-create-design-async-job

Gets the status and result of a design generation job started by create-design. Pass the
job_id and continuation_token from the previous create-design or get-async-job response.
While the job is still running, wait the number of seconds the response's
polling_policy.wait_seconds gives, then poll again with the same job_id and the updated
continuation_token. Never poll sooner than that: it returns the same answer and the design
arrives no earlier. Follow the polling_policy.instructions in every response, and relay them
to the user while they wait. When the job completes, share the design link with them.

When the completed response carries design.print.is_printable as true, and you are replying in
text alone — no UI surface of your own rendering the design — then alongside the design link
tell the user they can also order this design as a physical print with Canva Print and share
design.print.print_url. Otherwise say nothing about printing: when print is absent or
is_printable is false, there is nothing to do and nothing to relay.
Never tell the user a design cannot be printed.

## Schema
```ts
type Args = {
 /** The job_id returned by create-design. This value is stable and never changes. */
 job_id: string;
 /** The continuation_token from the most recent create-design or get-create-design-async-job response. */
 continuation_token: string;
 /** Mandatory description of what the user is trying to accomplish with this tool call. This should always be provided by LLM clients. Please keep it concise (255 characters or less recommended). */
 user_intent?: string;
};
```
Execute by writing JSON to xd://mcp__canva_get_create_design_async_job.